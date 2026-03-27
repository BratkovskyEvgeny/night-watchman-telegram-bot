"""
Night Watchman - Mistral AI Integration
Uses Mistral AI API for advanced spam detection with rate limiting.
Replaces Gemini scanner for Russian-speaking groups.
"""

import asyncio
import json
import logging
import os
import time
from collections import deque
from datetime import datetime, timezone
from typing import Dict, Optional

from config import Config
from redis_manager import RedisManager

logger = logging.getLogger(__name__)

MISTRAL_AVAILABLE = False
try:
    import httpx
    MISTRAL_AVAILABLE = True
except ImportError:
    logger.warning("httpx not installed. Mistral scanner disabled.")


class MistralScanner:
    """
    Spam scanner using Mistral AI API.
    Handles rate limiting to stay within API usage limits.
    Optimized for Russian-language content moderation.
    """
    
    MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"
    
    def __init__(self):
        self.config = Config()
        self.api_key = getattr(self.config, 'MISTRAL_API_KEY', None) or os.getenv("MISTRAL_API_KEY")
        self.model_name = getattr(self.config, 'MISTRAL_MODEL', 'mistral-small-latest')
        self.rpm_limit = getattr(self.config, 'MISTRAL_RPM_LIMIT', 10)
        self.enabled = (
            getattr(self.config, 'MISTRAL_ENABLED', True) and
            MISTRAL_AVAILABLE and
            bool(self.api_key)
        )
        
        # Rate limiting: Store timestamps of requests
        self._request_timestamps = deque()
        
        # Initialize Redis
        self.redis = RedisManager()
        
        if self.enabled:
            logger.info(f"✨ Mistral AI scanner initialized (Model: {self.model_name})")
        elif not self.api_key:
            logger.warning("⚠️ Mistral enabled but no API key found (MISTRAL_API_KEY). Disabling.")
            self.enabled = False
            
    async def _check_rate_limit(self) -> bool:
        """
        Check if we have quota to make a request.
        Uses Redis if available, otherwise falls back to local memory.
        """
        # USE REDIS if available (Global limit across all instances)
        if self.redis.enabled:
            is_limited = await self.redis.check_rate_limit("mistral:rpm", self.rpm_limit, 60)
            return not is_limited

        # Fallback: In-memory check
        now = time.time()
        
        # Remove timestamps older than 60 seconds
        while self._request_timestamps and self._request_timestamps[0] < now - 60:
            self._request_timestamps.popleft()
            
        # Check if we have room
        if len(self._request_timestamps) < self.rpm_limit:
            self._request_timestamps.append(now)
            return True
            
        return False
        
    async def scan_message(self, text: str, user_context: str = "", image_data: Optional[bytes] = None) -> Optional[Dict]:
        """
        Scan a message using Mistral AI.
        
        Args:
            text: Message text
            user_context: Additional context about user (e.g. "New user, joined 5 min ago")
            image_data: Optional image data (not supported by Mistral text API, ignored)
            
        Returns:
            Dict with keys: is_spam (bool), confidence (float), reasoning (str), reason (str)
            OR None if scan was skipped (rate limit, error, disabled)
        """
        if not self.enabled:
            return None
            
        if not text or len(text.strip()) < 10:
            return None
        
        # Check rate limit
        if not await self._check_rate_limit():
            logger.debug("⏳ Mistral rate limit reached. Skipping scan.")
            return None
            
        try:
            system_prompt = """Ты — бот-модератор Telegram-группы про разработку, AI и Web3.

Тематика группы: Python, Go, Rust, Solidity, веб-разработка, MLOps, LLMOps, AgentOps, мультиагентные системы, блокчейн, NFT, смарт-контракты, автоматизация (n8n, LangFlow).

Контекст: русскоязычная группа. Сообщения могут быть на русском или английском языке.

ЗАПРЕЩЁННЫЙ КОНТЕНТ (помечай как spam с высокой уверенностью):
- Крипто-мошенничество (удвоение денег, фейковые инвестиционные схемы, "гарантированный доход")
- Казино/азартные игры (промокоды, бонусы, фейковые выигрыши)
- Фишинговые ссылки (дрейнеры кошельков, фейковые аирдропы)
- Мошенничество с вакансиями (фейковые предложения работы с просьбой написать в ЛС)
- Нежелательная реклама/промо без разрешения
- Контент для взрослых (NSFW): порно, секс-услуги, эскорт
- Схемы быстрого заработка (пирамиды, хайп-проекты, обнал)
- Агрессивные приглашения написать в личные сообщения
- Терроризм, экстремизм, призывы к насилию
- Нацизм, фашизм, расизм, антисемитизм
- Продажа наркотиков, оружия, поддельных документов
- Детская порнография (немедленный бан)
- Политическая агитация и провокации (война, политические лидеры в провокационном контексте)
- Оскорбления по национальному, религиозному, расовому признаку

РАЗРЕШЁННЫЙ КОНТЕНТ (НЕ помечай как spam):
- Обычные приветствия ("Привет", "Как дела?", "Добрый день")
- Технические вопросы по Python, Go, Rust, Solidity, Web3, AI, ML
- Обсуждение MLOps, LLMOps, AgentOps, мультиагентных систем
- Вопросы про блокчейн, смарт-контракты, NFT (без мошенничества)
- Ссылки на GitHub, документацию, Habr, Medium, Stack Overflow
- Ссылки на крупные биржи (binance.com, bybit.com и т.д.)
- Нейтральное упоминание политических событий (без агитации)
- Обсуждение новостей без призывов к насилию
- Технические термины: MEV, sniper bot, front-running (это легитимные Web3-темы)

Контекст пользователя: {user_context}

Отвечай ТОЛЬКО в формате JSON:
{{
  "is_spam": boolean,
  "confidence": float (0.0 до 1.0),
  "category": "string (scam/casino/promo/safe/nsfw/recruitment/terrorism/drugs/nazism/politics/other)",
  "reasoning": "краткое объяснение на русском"
}}"""

            user_message = f'Сообщение для анализа: "{text}"'
            
            payload = {
                "model": self.model_name,
                "messages": [
                    {
                        "role": "system",
                        "content": system_prompt.format(user_context=user_context or "Нет данных")
                    },
                    {
                        "role": "user",
                        "content": user_message
                    }
                ],
                "temperature": 0.1,
                "max_tokens": 200,
                "response_format": {"type": "json_object"}
            }
            
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            async with httpx.AsyncClient(timeout=15.0) as client:
                response = await client.post(
                    self.MISTRAL_API_URL,
                    json=payload,
                    headers=headers
                )
                response.raise_for_status()
                
            response_data = response.json()
            result_text = response_data["choices"][0]["message"]["content"].strip()
            
            # Remove markdown code blocks if present
            if result_text.startswith("```json"):
                result_text = result_text[7:]
            if result_text.startswith("```"):
                result_text = result_text[3:]
            if result_text.endswith("```"):
                result_text = result_text[:-3]
                
            data = json.loads(result_text.strip())
            
            return {
                'is_spam': data.get('is_spam', False),
                'confidence': float(data.get('confidence', 0.0)),
                'reasoning': data.get('reasoning', 'Нет объяснения'),
                'reason': data.get('reasoning', 'Нет объяснения')  # Alias for compatibility
            }
            
        except json.JSONDecodeError as e:
            logger.error(f"Mistral JSON parse error: {e}")
            return None
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 429:
                logger.warning(f"⏳ Mistral rate limit (429): {e}")
            elif e.response.status_code in (401, 403):
                logger.error(f"❌ Mistral API auth error (check MISTRAL_API_KEY): {e}")
            else:
                logger.error(f"❌ Mistral HTTP error {e.response.status_code}: {e}")
            return None
        except Exception as e:
            error_msg = str(e).lower()
            if 'quota' in error_msg or 'rate' in error_msg:
                logger.warning(f"⏳ Mistral quota/rate limit: {e}")
            elif 'api' in error_msg or 'key' in error_msg:
                logger.error(f"❌ Mistral API error (check key): {e}")
            else:
                logger.error(f"❌ Mistral scan error: {e}")
            return None


# Global instance
_mistral_scanner = None


def get_mistral_scanner() -> MistralScanner:
    global _mistral_scanner
    if _mistral_scanner is None:
        _mistral_scanner = MistralScanner()
    return _mistral_scanner


# Compatibility alias — so existing code that imports get_gemini_scanner still works
def get_gemini_scanner():
    """Compatibility alias: returns Mistral scanner instead of Gemini."""
    return get_mistral_scanner()
