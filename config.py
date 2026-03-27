"""
Night Watchman Bot Configuration
Telegram Spam Detection & Moderation
"""

import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    # Telegram Settings
    BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")  # Where to send spam reports
    
    # Spam Detection Settings
    # NOTE: Keep keywords SPECIFIC to avoid false positives on normal messages.
    # Short/generic words like "casino", "per day", "send me" are NOT here — they're too broad.
    SPAM_KEYWORDS = [
        # Crypto scams (English) — specific phrases only
        "dm me for gains", "guaranteed profit", "100x guaranteed",
        "free airdrop", "claim now", "wallet connect", "validate wallet", "sync wallet",
        "make money fast", "be your own boss",
        "invest with me", "trading signals",
        "binary options", "forex signals",
        
        # AI scan triggers (low score 0.3 — triggers AI scan)
        "check bio", "link in bio", "bio link", "see bio",
        # NOTE: "sniper bot", "mev bot", "front run bot" removed — legitimate Web3 topics
        "passive income", "steady income",

        # Specific scam phrases
        "trading account is thriving",
        "provided financial assistance",
        "withdrawals are straightforward",
        "from food stamps to $",
        "profit Mrs @",
        "automated trading system based on market conditions",
        "avoids risky strategies like martingale",
        "aims for a daily performance of",
        "ea operates on the m5 timeframe",
        "compatible with all brokers",
        "manages sl/tp",
        "works 24/5 on mt4 and mt5",
        "funded account challenges",
        "send me a dm for more proof",
        "financial assistance", "seamless withdrawal", "transformed my trading journey",
        
        # Aggressive DM patterns (specific)
        "dm me now", "inbox me now", "message me now",
        "hit me up", "slide into",
        "drop a dm", "send a dm",
        
        # Trading/Forex Scam Patterns (specific)
        "consistently profitable", "consistently profit",
        "level up your trading",
        "profitable for over", "profitable strategy",
        "proven strategy", "proven method", "proven system",
        
        # Casino/Betting Spam (specific phrases)
        "welcome bonus", "1win", "1xbet", "melbet", "mostbet",
        "casino bonus", "poker bonus", "free spins",
        "winning streak", "top prize", "grab bonus", "telegram bonus",
        "$200 free", "$100 free", "$500 free",
        "52casino", "reward received",
        "sign up here:", "start playing today",
        
        # Adult/Porn (INSTANT BAN)
        "xxx", "porn", "p-o-r-n", "x x x", "p o r n",
        "onlyfans", "only fans", "adult content",
        "nudes", "sexy video", "hot video",
        
        # Russian Spam Patterns — SPECIFIC phrases only (avoid generic words)
        "пишите в лс", "пишите в личку",
        "напишите в лс", "напишите в личку",
        "пиши в лс", "пиши в личку",
        "стучите в лс", "стучите в личку",
        "заработок в день", "заработок в месяц",
        "зарабатывай дома", "зарабатывай из дома",
        "пассивный заработок",
        "гарантированный доход", "гарантированная прибыль",
        "торговые сигналы", "сигналы для торговли",
        "бинарные опционы", "форекс сигналы",
        "инвестируй со мной", "вложи и получи",
        "удвоение депозита", "удвоение вклада",
        "криптовалюта заработок", "крипто заработок",
        "бесплатный аирдроп", "получи токены бесплатно",
        "бонус при регистрации",
        "казино бонус", "покер бонус", "фриспины",
        "большой выигрыш", "выиграй сейчас",
        "ставка на спорт", "спортивные ставки",
        "1вин", "1хбет", "мелбет", "мостбет",
        "набор в команду", "набираю команду",
        "лёгкий заработок", "легкий заработок",
        "обучу бесплатно за результат",
        "ежедневные выплаты", "выплаты каждый день",
        "от 500 рублей в день", "от 1000 рублей в день",
        "от $100 в день", "от $200 в день",
        "схема заработка", "рабочая схема заработка",
        "нажми на ссылку", "перейди по ссылке",
        "подпишись на канал для заработка",
        "только сегодня успей", "мест осталось мало",
        "телеграм канал для заработка",
        "инвестиционный проект", "хайп проект", "hyip",
        "финансовая пирамида",
        "отмывание денег", "обнал",
        "интим услуги",
        "знакомства для взрослых", "горячие фото",
        "горячие видео", "откровенные фото",
        
        # Recruitment/Job Scam Patterns (specific)
        "opening recruitment", "opening a recruitment",
        "recruiting for a project", "recruitment for a project",
        "earnings from $", "income from $", "earn from $",
        "putting together a team", "putting together a small team",
        "looking for 2-3 people", "looking for two people",
        "full training and support",
        "daily payments", "everything is transparent",
        "1-2 hours per day", "1.5-2 hours per day",
        "send me a private message", "write to me at",
        
        # ==================== ЗАПРЕЩЁННЫЕ ТЕМЫ ====================
        # Эти слова дают низкий балл (0.3) и триггерят проверку через Mistral AI
        # Они НЕ вызывают автоматический бан — только флаг для проверки
        
        # Политика (триггер для AI-проверки)
        "путин", "лукашенко", "зеленский",
        "кгб", "фсб", "мвд", "нквд",
        "украина", "донбасс", "крым",
        "нато", "санкции против",
        "война на украине", "спецоперация",
        "оппозиция", "протест", "митинг",
        "политический заключённый", "политзаключённый",
        
        # Экстремизм / терроризм (триггер для AI-проверки)
        "джихад", "аллах акбар",
        "взрывчатка", "самодельная бомба",
        "теракт", "террористическая атака",
        "вербовка в", "вступай в отряд",
        
        # Наркотики (триггер для AI-проверки)
        "купить наркотики", "продам наркотики",
        "купить мефедрон", "купить амфетамин",
        "купить кокаин", "купить героин",
        "купить марихуану", "купить гашиш",
        "закладка наркотики", "закладчик",
        "купить спайс", "купить соль",
        "наркотики доставка", "наркотики телеграм",
        
        # ЛГБТ-пропаганда (триггер для AI-проверки)
        "лгбт пропаганда", "гей пропаганда",
        "трансгендер пропаганда",
        
        # Нацизм / расизм (триггер для AI-проверки)
        "нацизм", "нацист", "фашизм", "фашист",
        "белое превосходство", "арийская раса",
        "хайль", "свастика",
        "расизм", "расист",
        "антисемитизм", "антисемит",
        
        # Секс / порно (триггер для AI-проверки — явные уже в INSTANT_BAN)
        "секс видео", "секс фото", "секс чат",
        "виртуальный секс", "секс за деньги",
        "проститутка", "эскорт",
        "детское порно", "педофилия",
    ]
    
    # INSTANT BAN keywords (no warnings, immediate ban)
    # NOTE: Only VERY SPECIFIC phrases here — avoid generic words that appear in normal conversation
    INSTANT_BAN_KEYWORDS = [
        # Adult/Porn
        "xxx", "porn", "p-o-r-n", "x x x", "p o r n",
        "onlyfans", "only fans", "nudes",
        # Casino/Betting (specific brand names and phrases)
        "1win", "1xbet", "xwin", "22bet", "melbet", "mostbet",
        "52casino", "52 casino", ".52casino.cc", "52casino.cc",
        "casino bonus", "welcome bonus", "free spins",
        "winning streak", "top prize", "grab bonus", "telegram bonus",
        "on your balance", "activate promo",
        "play anywhere", "bet220", "promocasbot",
        "reward received", "your reward has been", "reward has been successfully",
        "won $100", "won $200", "$100 instantly",
        "promo code \"lucky", "enter promo code", "dont forget: enter promo",
        "start playing today",
        # Scam DM patterns (specific)
        "dm me now", "inbox me now", "message me now",
        # Recruitment scam instant ban patterns
        "write \"+\"", "leave a \"+\"", "send \"+\"",
        "write + in private", "leave + here",
        "earnings from $1", "income: starting at $",
        "earn a steady extra $", "extra $500", "extra $1,000",
        "$120 per day", "$190 per day", "$250 per day",
        "$1050 per week", "$1,050 per week", "$1000 per week",

        # Specific scam phrases
        "trading account is thriving",
        "provided financial assistance",
        "withdrawals are straightforward",
        "from food stamps to $",
        "profit Mrs @",
        "automated trading system based on market conditions",
        "avoids risky strategies like martingale",
        "aims for a daily performance of",
        "ea operates on the m5 timeframe",
        "compatible with all brokers",
        "manages sl/tp",
        "works 24/5 on mt4 and mt5",
        "funded account challenges",
        "send me a dm for more proof",
        
        # Russian instant ban patterns (мгновенный бан — только специфические фразы)
        "пишите в лс срочно", "пишите в личку срочно",
        "напишите мне срочно",
        "1вин", "1хбет", "мелбет", "мостбет", "1win.ru", "1xbet.ru",
        "казино бонус", "фриспины",
        "вы выиграли", "поздравляем вы выиграли",
        "активируй промокод", "введи промокод",
        "заработок от $120 в день", "заработок от $190 в день",
        "заработок от $250 в день",
        "доход от 1000 в день", "доход от 5000 в день",
        "напиши \"+\"", "оставь \"+\"", "напиши плюс",
        "интим фото", "интим видео",
        "эскорт услуги", "услуги интим",
        "обнал", "обналичивание", "отмыв денег",
        "хайп проект", "hyip проект",
        "финансовая пирамида",
        
        # ==================== ЗАПРЕЩЁННЫЙ КОНТЕНТ — МГНОВЕННЫЙ БАН ====================
        
        # Детское порно / педофилия (абсолютный запрет)
        "детское порно", "детская порнография", "педофилия",
        "child porn", "child pornography", "pedophilia",
        "cp telegram", "cp channel",
        
        # Терроризм / экстремизм (абсолютный запрет)
        "аллах акбар смерть", "смерть неверным",
        "взорвать", "самодельная бомба", "изготовить взрывчатку",
        "вступай в игил", "вступай в isis", "вступай в даиш",
        "джихад против", "газават",
        "убить президента", "убить политика",
        "теракт планируем", "готовим теракт",
        
        # Нацизм / фашизм (абсолютный запрет)
        "хайль гитлер", "heil hitler",
        "зиг хайль", "sieg heil",
        "нацисты победят", "слава нацистам",
        "смерть евреям", "смерть чёрным", "смерть мусульманам",
        "death to jews", "death to blacks",
        "белое превосходство", "white supremacy",
        "арийская раса превосходит",
        
        # Продажа наркотиков (абсолютный запрет)
        "купить мефедрон", "продам мефедрон",
        "купить амфетамин", "продам амфетамин",
        "купить кокаин", "продам кокаин",
        "купить героин", "продам героин",
        "купить спайс", "продам спайс",
        "купить соль наркотик", "продам соль наркотик",
        "закладка наркотики", "закладчик наркотики",
        "наркотики доставка", "наркотики телеграм",
        "купить марихуану доставка", "купить гашиш доставка",
        "mdma купить", "lsd купить", "экстази купить",
        
        # Мошенничество с документами
        "купить паспорт", "продам паспорт",
        "купить диплом", "продам диплом",
        "купить права", "продам права",
        "поддельные документы", "фальшивые документы",
        
        # Оружие (незаконная продажа)
        "купить оружие", "продам оружие",
        "купить пистолет нелегально", "продам пистолет нелегально",
        "купить автомат нелегально",
    ]
    
    # Whitelisted terms - NEVER trigger spam even if they contain keywords
    # This prevents false positives for legitimate questions
    WHITELISTED_PHRASES = [
        # Legitimate questions about promo codes
        "как получить промокод",
        "где найти промокод",
        "есть ли промокод",
        "промокод для",
        "реферальный код для",
        "как использовать промокод",
        # Legitimate trading discussion
        "стратегия торговли",
        "торговая стратегия",
        "анализ рынка",
        "технический анализ",
    ]
    
    # Money/Dollar emojis - suspicious when used by new users
    # These are often used in scam/promo messages
    MONEY_EMOJIS = ['💰', '💵', '💸', '🤑', '💲', '💳', '🏧', '💎', '🪙', '💴', '💶', '💷']
    
    # New user money emoji detection settings
    MONEY_EMOJI_CHECK_ENABLED = True
    MONEY_EMOJI_NEW_USER_HOURS = 48  # Check users who joined within this time
    MONEY_EMOJI_MIN_REP = 1  # Users with less than this rep are flagged
    MONEY_EMOJI_THRESHOLD = 2  # Number of money emojis to trigger (2+ = suspicious)
    MONEY_EMOJI_ACTION = "delete_and_warn"  # "delete", "delete_and_warn", "delete_and_mute"
    
    # Suspicious URL patterns
    SUSPICIOUS_DOMAINS = [
        "bit.ly", "tinyurl", "t.co", "goo.gl",  # URL shorteners (often abused)
        "telegram.me", "t.me",  # External telegram links
        # Add known scam domains
    ]
    
    # Whitelisted domains (always allowed)
    WHITELISTED_DOMAINS = [
        # Crypto / Finance
        "coingecko.com",
        "coinmarketcap.com",
        "tradingview.com",
        "binance.com",
        "bybit.com",
        "okx.com",
        "huobi.com",
        "kucoin.com",
        "gate.io",
        "kraken.com",
        "coinbase.com",
        "etherscan.io",
        "bscscan.com",
        "polygonscan.com",
        "solscan.io",
        "opensea.io",
        "uniswap.org",
        "aave.com",
        "compound.finance",
        
        # App Stores
        "apps.apple.com",
        "play.google.com",
        
        # Tech / Dev resources (для канала про разработку, AI и Web3)
        "github.com",
        "gitlab.com",
        "stackoverflow.com",
        "docs.python.org",
        "python.org",
        "golang.org",
        "go.dev",
        "rust-lang.org",
        "doc.rust-lang.org",
        "soliditylang.org",
        "docs.soliditylang.org",
        "npmjs.com",
        "pypi.org",
        "crates.io",
        "docker.com",
        "hub.docker.com",
        "kubernetes.io",
        "aws.amazon.com",
        "cloud.google.com",
        "azure.microsoft.com",
        "vercel.com",
        "netlify.com",
        "railway.app",
        "heroku.com",
        
        # AI / ML / NLP / LLM resources
        "openai.com",
        "anthropic.com",
        "mistral.ai",
        "huggingface.co",
        "arxiv.org",
        "paperswithcode.com",
        "langchain.com",
        "n8n.io",
        "langflow.org",
        "llamaindex.ai",
        "docs.llamaindex.ai",
        "python.langchain.com",
        "js.langchain.com",
        "ollama.ai",
        "ollama.com",
        "groq.com",
        "together.ai",
        "replicate.com",
        "cohere.com",
        "ai.google.dev",
        "deepmind.google",
        "pytorch.org",
        "tensorflow.org",
        "keras.io",
        "scikit-learn.org",
        "pandas.pydata.org",
        "numpy.org",
        "matplotlib.org",
        "jupyter.org",
        "kaggle.com",
        "wandb.ai",
        "mlflow.org",
        "dvc.org",
        "ray.io",
        "modal.com",
        "bentoml.com",
        "fastapi.tiangolo.com",
        "pydantic.dev",
        "docs.pydantic.dev",
        "celery.readthedocs.io",
        "redis.io",
        "postgresql.org",
        "mongodb.com",
        "clickhouse.com",
        "qdrant.tech",
        "weaviate.io",
        "pinecone.io",
        "chroma.run",
        "milvus.io",
        
        # Web3 / Blockchain
        "ethereum.org",
        "solana.com",
        "polygon.technology",
        "hardhat.org",
        "truffle-suite.io",
        "web3.js.readthedocs.io",
        "ethers.io",
        "openzeppelin.com",
        "chainlink.com",
        "ipfs.io",
        
        # News / Media
        "ru.wikipedia.org",
        "wikipedia.org",
        "rbc.ru",
        "kommersant.ru",
        "vedomosti.ru",
        "tass.ru",
        "ria.ru",
        "interfax.ru",
        "cbr.ru",
        "habr.com",
        "medium.com",
        "dev.to",
        "youtube.com",
        "youtu.be",
    ]
    
    # New user settings
    NEW_USER_LINK_BLOCK_HOURS = 24  # Block links from users < 24h in group
    NEW_USER_WARNING_THRESHOLD = 2  # Warnings before mute
    
    # Rate limiting
    MAX_MESSAGES_PER_MINUTE = 10  # Flag users sending too fast
    DUPLICATE_MESSAGE_THRESHOLD = 3  # Same message X times = spam
    
    # Actions
    AUTO_DELETE_SPAM = True
    AUTO_WARN_USER = True
    AUTO_MUTE_AFTER_WARNINGS = 3
    AUTO_BAN_AFTER_WARNINGS = 5  # Ban after X warnings
    MUTE_DURATION_HOURS = 24
    
    # Bad Language Detection
    BAD_LANGUAGE_ENABLED = True
    BAD_LANGUAGE_WORDS = [
        # English Profanity
        "fuck", "shit", "bitch", "asshole", "bastard",
        "dick", "cock", "pussy",
        
        # Russian Profanity — мат (корневые слова, покрывают большинство форм)
        "блядь", "блять", "блядина",
        "пизда", "пиздец", "пиздить", "пиздёж", "пиздабол",
        "ёбаный", "ёб твою", "ёбнутый", "ёблан", "еблан",
        "хуй", "хуйня", "хуёво", "хуйло", "хуесос",
        "залупа",
        "мудак", "мудила", "мудозвон",
        "сука", "сучка",
        "ублюдок",
        "пидор", "пидорас",
        "шлюха", "шлюшка",
        "долбоёб",
        "нахуй", "на хуй",
        "иди нахуй", "пошёл нахуй", "пошла нахуй",
        "ёб твою мать", "твою мать",
        "говно", "говнюк",
        "жопа",
        "задница",
        "мразь",
        "падла",
        "гнида",
        "козёл",
        "сволочь",
        "подонок",
        "тварь",
        "скотина",
        "урод",
        "чмо",
        "лошара",
        "выблядок",
        "гандон",
    ]
    BAD_LANGUAGE_ACTION = "delete_and_warn"  # "warn", "delete", "delete_and_warn", "mute"
    
    # New User Verification
    VERIFY_NEW_USERS = True
    MIN_ACCOUNT_AGE_DAYS = 7  # Require account to be at least 7 days old
    SUSPICIOUS_USERNAME_PATTERNS = [
        r'^[0-9]+$',  # Only numbers
        r'^user[0-9]+$',  # user12345 pattern
        r'^telegram[0-9]+$',  # telegram123 pattern
        r'.*spam.*',  # Contains "spam"
        r'.*scam.*',  # Contains "scam"
    ]
    AUTO_BAN_SUSPICIOUS_JOINS = False  # Auto-ban or just restrict
    RESTRICT_NEW_USERS_HOURS = 24  # Restrict new users for X hours
    
    # Bot Account Blocking
    BLOCK_BOT_JOINS = True  # Auto-ban bot accounts that join
    BOT_USERNAME_PATTERNS = [
        r'.*bot$',  # Ends with "bot"
        r'.*_bot$',  # Ends with "_bot"
    ]
    
    # Anti-Raid Protection
    ANTI_RAID_ENABLED = True
    RAID_DETECTION_WINDOW_MINUTES = 5  # Check last 5 minutes
    RAID_THRESHOLD_USERS = 10  # If 10+ new users join in window, it's a raid
    
    # CAS (Combot Anti-Spam) Integration
    CAS_ENABLED = True  # Check new members against CAS database
    CAS_AUTO_BAN = True  # Auto-ban users found in CAS database
    CAS_API_URL = "https://api.cas.chat/check"  # CAS API endpoint
    
    # Media/Sticker Spam Detection
    MEDIA_SPAM_DETECTION_ENABLED = False  # Disabled as requested (was True)
    BLOCK_MEDIA_FROM_NEW_USERS = True  # Block photos/videos/stickers from new users
    MEDIA_NEW_USER_HOURS = 24  # Hours before new users can send media
    BLOCK_STICKERS_FROM_NEW_USERS = True  # Block stickers from new users
    BLOCK_GIFS_FROM_NEW_USERS = True  # Block GIFs/animations from new users
    MAX_MEDIA_PER_MINUTE = 10  # Increased from 3 to 10 (campaign mode)
    MEDIA_SPAM_ACTION = "delete_and_warn"  # "delete", "delete_and_warn", "delete_and_mute"
    
    # Forward Message Handling
    BLOCK_FORWARDS = True
    FORWARD_ALLOW_ADMINS = True
    FORWARD_ALLOW_VIP = True
    FORWARD_INSTANT_BAN = True  # INSTANT BAN on forward (not mute) - stops spam immediately
    FORWARD_INSTANT_MUTE = False  # Mute user immediately on forward (legacy, use INSTANT_BAN instead)
    FORWARD_BAN_ON_REPEAT = True  # Ban if user forwards again after mute (if not using instant ban)
    
    # Premium/Custom Emoji Spam Detection
    PREMIUM_EMOJI_SPAM_ENABLED = True
    PREMIUM_EMOJI_THRESHOLD = 3  # 3+ custom/premium emojis = spam (normal users rarely use this many)
    PREMIUM_EMOJI_NEW_USER_BAN = True  # Instant ban new users (<48h) with premium emoji spam
    
    # Welcome Message
    SEND_WELCOME_MESSAGE = False  # Don't auto-send welcome (users can use /guidelines)
    WELCOME_MESSAGE = """👋 Добро пожаловать в группу!

📋 <b>Правила:</b>
• Никакого спама и мошенничества
• Никакой нецензурной лексики
• Уважайте друг друга
• Реклама без разрешения запрещена

⚠️ Нарушения влекут предупреждения, мут или бан."""
    
    # Auto-delete join/exit messages
    DELETE_JOIN_EXIT_MESSAGES = True
    
    # Foreign Language Detection
    # Only Russian and English are allowed in this group.
    # Messages in Chinese, Korean, Arabic, Japanese, Thai, Vietnamese will be blocked.
    BLOCK_NON_INDIAN_LANGUAGES = True  # Enabled — block non-Russian/non-English languages
    NON_INDIAN_LANGUAGES = [
        'chinese', 'korean', 'japanese', 'arabic', 'thai', 'vietnamese'
        # Note: 'russian' is NOT in this list — it's the primary language of this group
        # English is also allowed (Latin script)
    ]
    AUTO_BAN_NON_INDIAN_SPAM = True  # Auto-ban if foreign language + suspicious content
    
    # Bot Message Auto-Delete
    AUTO_DELETE_BOT_MESSAGES = True
    BOT_MESSAGE_DELETE_DELAY_SECONDS = 60  # Delete after 1 minute
    
    # Admin Commands
    ADMIN_COMMANDS_ENABLED = True
    
    # ==================== COMMAND ROUTING ====================
    # Redirect crypto/trading commands to specific topic instead of warning users
    
    # Night Watchman bot commands (always allowed everywhere)
    BOT_COMMANDS = [
        '/start', '/help', '/guidelines', '/admins', '/rep', '/leaderboard',
        '/report', '/warn', '/ban', '/mute', '/unwarn', '/enhance', '/cas',
        '/stats', '/analytics'
    ]
    
    # Crypto/trading commands that should be redirected to Market Intelligence topic
    CRYPTO_COMMANDS = [
        # Price commands
        '/btc', '/eth', '/sol', '/xrp', '/bnb', '/ada', '/doge', '/dot',
        '/matic', '/link', '/avax', '/shib', '/ltc', '/atom', '/uni',
        '/btcusd', '/ethusd', '/solusd', '/xrpusd',
        # Trading commands
        '/price', '/chart', '/ta', '/signal', '/signals',
        '/alert', '/alerts', '/market', '/markets', '/trade', '/trading',
    ]
    
    # Comprehensive list of crypto ticker symbols (to prevent false spam detection)
    # Auto-generated from exchange API - covers 450+ tokens available for trading
    CRYPTO_TICKERS = [
        # A-B
        '0g', '1inch', '2z', 'a8', 'aave', 'ach', 'acs', 'ada', 'aero', 'aevo',
        'afc', 'agi', 'agix', 'agld', 'aioz', 'aixbt', 'akt', 'akash', 'alch', 'algo',
        'alt', 'ami', 'anime', 'ankr', 'ao', 'ape', 'apex', 'apt', 'ar', 'arb',
        'arkm', 'art', 'arty', 'aster', 'ath', 'atom', 'audio', 'aurora', 'ava', 'avail',
        'avax', 'avl', 'avnt', 'axl', 'axs', 'b3', 'baby1', 'bal', 'ban', 'bard',
        'bat', 'bb', 'bbsol', 'bch', 'bdxn', 'beam', 'bel', 'bera', 'bico', 'bigtime',
        'blast', 'blur', 'bmt', 'bnb', 'bnt', 'bob', 'boba', 'bomb', 'bome', 'bone',
        'bonk', 'br', 'brett', 'bsv', 'btc', 'btg', 'btt',
        # C-D
        'c98', 'cake', 'camp', 'carv', 'cat', 'cate', 'cati', 'cbk', 'cc', 'celo',
        'celr', 'cfg', 'cfx', 'cgpt', 'chsb', 'chz', 'city', 'ckb', 'cloud', 'cmeth',
        'coinx', 'common', 'comp', 'cook', 'cookie', 'cope', 'coq', 'core', 'corn', 'cpool',
        'cro', 'crv', 'cspr', 'cta', 'ctc', 'ctsi', 'cudis', 'cvx', 'cyber', 'dai',
        'dash', 'dbr', 'dcr', 'deep', 'degen', 'dent', 'dfinity', 'dgb', 'diam', 'dmail',
        'doge', 'dogs', 'dolo', 'dood', 'dot', 'dpx', 'drift', 'dusk', 'dydx', 'dym',
        # E-F
        'eat', 'egld', 'eigen', 'elx', 'ena', 'enj', 'ens', 'enso', 'eos', 'ept',
        'era', 'es', 'ese', 'etc', 'eth', 'ethfi', 'ethw', 'ever', 'fet', 'ff',
        'fhe', 'fida', 'fil', 'fitfi', 'flip', 'flock', 'floki', 'flow', 'flr', 'fluid',
        'flux', 'fort', 'foxy', 'frag', 'frax', 'ftt', 'ftm', 'fuel', 'fxs',
        # G-H
        'gaib', 'gala', 'game', 'glm', 'glmr', 'gmt', 'gmx', 'goat', 'gods', 'gps',
        'grail', 'grass', 'grt', 'gst', 'gt', 'gtai', 'gusd', 'haedal', 'hbar', 'hft',
        'hive', 'hmstr', 'hnt', 'holo', 'home', 'hook', 'hpos', 'ht', 'htx', 'huma',
        'hype', 'hyper',
        # I-J-K
        'icnt', 'icp', 'icx', 'id', 'ilv', 'imx', 'init', 'inj', 'insp', 'inter',
        'io', 'iota', 'iotx', 'ip', 'izi', 'jasmy', 'jet', 'joe', 'jones', 'jst',
        'jto', 'jup', 'juv', 'kaia', 'kas', 'kasta', 'kava', 'kcs', 'kda', 'kilo',
        'kmno', 'knc', 'ksm', 'kub',
        # L-M
        'l3', 'la', 'ladys', 'lava', 'layer', 'lbtc', 'ldo', 'leo', 'linea', 'link',
        'litkey', 'll', 'lmwr', 'lpt', 'lqty', 'lrc', 'ltc', 'luna', 'lunai', 'lunc',
        'lusd', 'magic', 'major', 'mana', 'mango', 'manta', 'masa', 'mask', 'matic', 'mavia',
        'mbox', 'mbx', 'mc', 'mcrt', 'me', 'mee', 'meme', 'memefi', 'merl', 'met',
        'metax', 'metis', 'meth', 'mew', 'milk', 'mim', 'mina', 'mir', 'mkr', 'mmt',
        'mngo', 'mnt', 'moca', 'mode', 'mog', 'mon', 'monpro', 'morpho', 'move', 'movr',
        'mplx', 'mvl', 'mx', 'myro',
        # N-O
        'naka', 'navx', 'near', 'neiro', 'neo', 'neon', 'newt', 'nexo', 'nft', 'nibi',
        'night', 'nkn', 'nmt', 'nom', 'not', 'nrn', 'ns', 'nym', 'oas', 'obol',
        'obt', 'ocean', 'odos', 'ohm', 'okb', 'ol', 'olas', 'om', 'omg', 'ondo',
        'one', 'ont', 'op', 'orca', 'order', 'ordi', 'oxt',
        # P-Q
        'paal', 'parti', 'pell', 'pendle', 'pengu', 'people', 'pepe', 'perp', 'pineye', 'pirate',
        'pixel', 'plume', 'plutus', 'pnut', 'pol', 'poly', 'ponke', 'popcat', 'port', 'port3',
        'portal', 'prcl', 'prime', 'prove', 'psg', 'psyop', 'pstake', 'puff', 'puffer', 'pump',
        'purse', 'pyr', 'pyth', 'pyusd', 'qnt', 'qorpo', 'qtum',
        # R-S
        'raca', 'rad', 'rare', 'rats', 'ray', 'rdnt', 'recall', 'red', 'render', 'req',
        'resolv', 'rlc', 'rlusd', 'rndr', 'roam', 'ron', 'ronin', 'root', 'rose', 'rpl',
        'rsr', 'rss3', 'rune', 'rvn', 'saber', 'safe', 'sahara', 'samo', 'sand', 'saros',
        'sats', 'sbr', 'sc', 'sca', 'scr', 'scroll', 'scrt', 'sd', 'sei', 'send',
        'seraph', 'serum', 'sfp', 'sfund', 'shards', 'shib', 'sidus', 'sign', 'silo', 'sis',
        'skate', 'skl', 'sky', 'slerf', 'slnd', 'slp', 'snx', 'sol', 'solo', 'solv',
        'somi', 'sonic', 'soso', 'spec', 'spell', 'spk', 'spx', 'sqd', 'sqr', 'srm',
        'ssv', 'stable', 'steem', 'step', 'steth', 'storj', 'stream', 'strk', 'stx', 'sui',
        'sun', 'sundog', 'super', 'supra', 'sushi', 'svl', 'sweat', 'swell', 'sxt', 'synd',
        'sys',
        # T-U-V
        'ta', 'tac', 'tai', 'taiko', 'tao', 'tel', 'tfuel', 'thena', 'theta', 'tia',
        'time', 'tnsr', 'token', 'ton', 'toshi', 'towns', 'trc', 'tree', 'trump', 'trvl',
        'trx', 'tulip', 'tuna', 'turbo', 'turbos', 'tusd', 'twt', 'ulti', 'uma', 'uni',
        'usd1', 'usdc', 'usdd', 'usde', 'usdp', 'usdt', 'usdtb', 'usdy', 'ust', 'ustc',
        'uxlink', 'vana', 'vanry', 'velo', 'venom', 'vet', 'vic', 'vinu', 'vra', 'vtho',
        'vvv',
        # W-X-Y-Z
        'w', 'wal', 'waves', 'wax', 'waxp', 'wbtc', 'wct', 'weeth', 'wemix', 'wen',
        'wet', 'weth', 'wif', 'wld', 'wlfi', 'woo', 'wojak', 'wrx', 'xai', 'xan',
        'xaut', 'xava', 'xcad', 'xdc', 'xec', 'xem', 'xion', 'xlm', 'xmr', 'xo',
        'xpl', 'xrp', 'xter', 'xtz', 'xusd', 'x2y2', 'yb', 'yfi', 'ygg', 'zbt',
        'zec', 'zen', 'zent', 'zeta', 'zex', 'zig', 'zil', 'zk', 'zkc', 'zkj',
        'zkl', 'zksync', 'zora', 'zrc', 'zro', 'zrx', 'ztx',
    ]
    
    # Funding rate commands - redirected to Futures Funding Alerts topic
    FUNDING_COMMANDS = [
        '/funding', '/fundingrate', '/fundingrates',
        '/fr',  # Short for funding rate
    ]
    # Also match /funding_btc, /funding_eth, etc. (handled in code)
    
    # Enable crypto command redirection
    CRYPTO_COMMAND_REDIRECT_ENABLED = False  # Disabled for Russian group (no Mudrex topics)
    
    # Topic ID for Market Intelligence (where crypto price commands should go)
    MARKET_INTELLIGENCE_TOPIC_ID = int(os.getenv("MARKET_TOPIC_ID", "0"))
    MARKET_INTELLIGENCE_TOPIC_NAME = "Рынок и аналитика"
    MARKET_INTELLIGENCE_TOPIC_LINK = ""
    
    # Topic ID for Futures Funding Alerts (where funding commands should go)
    FUNDING_ALERTS_TOPIC_ID = int(os.getenv("FUNDING_TOPIC_ID", "0"))
    FUNDING_ALERTS_TOPIC_NAME = "Фьючерсы и фандинг"
    FUNDING_ALERTS_TOPIC_LINK = ""
    
    # PnL topic: never delete any image posted here
    PNL_TOPIC_ID = int(os.getenv("PNL_TOPIC_ID", "0"))
    
    # Message to show when redirecting crypto commands
    CRYPTO_COMMAND_REDIRECT_MESSAGE = """💡 <b>Не та тема!</b>

Эта команда работает в теме <a href="{topic_link}">{topic_name}</a>.

Пожалуйста, используйте крипто-команды там! 📊"""
    
    # Message to show when redirecting funding commands
    FUNDING_COMMAND_REDIRECT_MESSAGE = """💡 <b>Не та тема!</b>

Команды фандинга работают в теме <a href="{topic_link}">{topic_name}</a>.

Пожалуйста, используйте /funding там! 📈"""
    
    # Admin User IDs (can access /analytics via DM)
    # Add your Telegram user ID here
    ADMIN_USER_IDS = [
        int(x) for x in os.getenv("ADMIN_USER_IDS", "").split(",") if x.strip()
    ] if os.getenv("ADMIN_USER_IDS") else []
    
    # Analytics Settings
    ANALYTICS_ENABLED = True
    ANALYTICS_RETENTION_DAYS = 90  # Keep data for 90 days
    ANALYTICS_DATA_DIR = os.getenv("ANALYTICS_DATA_DIR", "data")  # Configurable for Railway volumes
    
    # Mistral AI Integration (replaces Gemini)
    GEMINI_ENABLED = True  # Keep flag name for compatibility, but uses Mistral
    GEMINI_API_KEY = os.getenv("MISTRAL_API_KEY")  # Mistral API key
    GEMINI_MODEL = "mistral-small-latest"  # Mistral model
    GEMINI_RPM_LIMIT = 10  # Conservative limit
    GEMINI_CONFIDENCE_THRESHOLD = 0.8  # Trust AI if it's 80% sure
    GEMINI_SCAN_THRESHOLD = 0.3  # Only scan messages that are already slightly suspicious
    
    # Mistral AI settings (explicit)
    MISTRAL_ENABLED = True
    MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
    MISTRAL_MODEL = "mistral-small-latest"  # Fast and cheap model
    MISTRAL_RPM_LIMIT = 10
    MISTRAL_CONFIDENCE_THRESHOLD = 0.8
    MISTRAL_SCAN_THRESHOLD = 0.3
    
    # ==================== NEW FEATURES ====================
    
    # Custom Commands
    GUIDELINES_MESSAGE = """📋 <b>Правила сообщества</b>

Добро пожаловать в авторский канал про разработку, AI и Web3!

<i>Группа активно модерируется для поддержания качества общения и безопасности участников.</i>

━━━━━━━━━━━━━━━━━━━━

🎯 <b>Темы сообщества</b>

• 🤖 Мультиагентные системы, MLOps/LLMOps/AgentOps
• ⛓️ Блокчейн, NFT и смарт-контракты
• ⚙️ Автоматизация процессов (n8n, LangFlow)
• 🐍 Python, Go, Rust, Solidity и другие языки
• 🌐 Веб-разработка и Web3
• 💡 Обмен опытом и помощь новичкам

━━━━━━━━━━━━━━━━━━━━

🔏 <b>Правила поведения</b>

<b>1. Уважайте друг друга</b>
Вежливость обязательна. Никакого троллинга, оскорблений, дискриминации и личных нападок.

<b>2. Никакого спама и рекламы</b>
Запрещено публиковать рекламу, реферальные коды и промо без разрешения администрации. Повторные нарушения = бан.

<b>3. Не флудите</b>
Ведите содержательные беседы по теме. Никакого флуда и повторяющихся сообщений.

<b>4. Запрещённые темы</b>
Политика, нацизм, расизм, порно, наркотики, терроризм, экстремизм — немедленный бан.

<b>5. Защищайте свои данные</b>
Никогда не публикуйте приватные ключи, seed-фразы, пароли или данные аккаунтов.

━━━━━━━━━━━━━━━━━━━━

📚 <b>Что разрешено и что нет</b>

✅ <b>Приветствуется</b>
• «Как реализовать мультиагентную систему на LangChain?»
• «Какой паттерн лучше для смарт-контракта на Solidity?»
• «Как настроить n8n для автоматизации?»
• Ссылки на GitHub, документацию, статьи на Habr/Medium

❌ <b>Запрещено</b>
• Реклама и промо без разрешения
• Мошеннические схемы, казино, финансовые пирамиды
• Политические провокации
• Контент 18+

━━━━━━━━━━━━━━━━━━━━

🚨 <b>Полномочия администрации</b>

Администраторы могут удалять любой контент или пользователей, нарушающих дух сообщества. Баны могут выдаваться без предупреждения за серьёзные или повторные нарушения.

━━━━━━━━━━━━━━━━━━━━

🙌 <b>Напоследок</b>

Если вы здесь, чтобы учиться, строить и развиваться — добро пожаловать.

Если вы здесь, чтобы спамить или мошенничать — вы не по адресу.

<i>Защищено Night Watchman 🌙</i>"""
    
    HELP_MESSAGE = """🌙 <b>Команды Night Watchman</b>

<b>Для всех:</b>
/guidelines - Правила сообщества
/help - Это сообщение
/admins - Позвать администраторов
/report - Пожаловаться на сообщение (ответьте на него)
/rep - Проверить свою репутацию
/leaderboard - Топ участников за всё время
/leaderboard 7 - Топ участников за 7 дней
/leaderboard 30 - Топ участников за 30 дней

<b>Для администраторов:</b>
/warn - Предупредить пользователя (ответьте на сообщение)
/mute - Замутить пользователя (ответьте на сообщение)
/ban - Забанить пользователя (ответьте на сообщение)
/unwarn - Снять предупреждения (ответьте на сообщение)
/enhance - Дать +15 очков репутации (ответьте на сообщение)
/stats - Статистика бота
/analytics - Аналитика группы (в ЛС)

<b>📊 Начисление очков репутации:</b>
Ежедневная активность: +5 очков
Обоснованная жалоба на спам: +10 очков
Бонус за 7 дней подряд: +5 очков
Бонус за 30 дней подряд: +10 очков
Повышение от администратора (/enhance): +15 очков
Предупреждение: -10 очков
Мут: -25 очков
Снятие мута (ложное срабатывание): +15 очков

<i>Защищено Night Watchman 🌙</i>"""

    # Safety Tip Message (shown when scammy spam is detected)
    SAFETY_TIP_MESSAGE = """
🛡 <b>Предупреждение безопасности:</b>
• Никогда не передавайте OTP-коды, пароли или приватные ключи.
• Не подключайте кошелёк к неизвестным сайтам.
• Невероятная прибыль = мошенничество. Всегда проверяйте сами (DYOR).
• Будьте осторожны при общении с незнакомцами в личных сообщениях."""
    
    # Reputation System (Points only - no perks/restrictions)
    # Points are for tracking engagement and can be used for campaigns
    REPUTATION_ENABLED = True
    REP_DAILY_ACTIVE = 5             # Points for daily activity (increased from 1)
    REP_VALID_REPORT = 10            # Points for valid spam report
    REP_WARNING_PENALTY = 10         # Points lost for warning
    REP_MUTE_PENALTY = 25            # Points lost for mute
    REP_UNMUTE_BONUS = 15            # Points for being unmuted (false positive)
    REP_ADMIN_ENHANCEMENT = 15       # Points for admin emoji enhancement on user's message (max once per message)
    REP_7DAY_STREAK_BONUS = 5        # Extra points for 7-day active streak (total: 7x5 + 5 = 40)
    REP_30DAY_STREAK_BONUS = 10      # Extra points for 30-day active streak (total: 30x5 + 10 = 160)
    REP_EXCLUDE_ADMINS = True        # Exclude admins from reputation tracking
    
    # Reputation Levels (display only - NO perks/restrictions)
    REP_LEVEL_MEMBER = 50       # Display level only
    REP_LEVEL_TRUSTED = 200     # Display level only
    REP_LEVEL_VIP = 500         # Display level only
    
    # Forward Detection (applies to ALL users equally)
    BLOCK_FORWARDS = True
    FORWARD_ALLOW_ADMINS = True
    # REMOVED: VIP forward bypass - forwards blocked for everyone except admins
    
    # Username Requirement
    REQUIRE_USERNAME = True
    USERNAME_GRACE_PERIOD_HOURS = 24  # Hours before kick
    USERNAME_WARNING_MESSAGE = """⚠️ <b>Требуется имя пользователя</b>

Пожалуйста, установите имя пользователя (username) в Telegram, чтобы участвовать в этой группе.

Перейдите в Настройки → Имя пользователя.

У вас есть 24 часа, после чего вы будете удалены из группы."""
    
    # Report System
    REPORT_ENABLED = True
    REPORT_COOLDOWN_SECONDS = 60  # Prevent report spam
    
    # Logging
    LOG_FILE = "logs/night_watchman.log"
    LOG_LEVEL = "INFO"
    
    # ==================== INTELLIGENT MODERATION FEATURES ====================
    
    # User Behavior Profiling
    BEHAVIOR_PROFILING_ENABLED = True
    BEHAVIOR_ANOMALY_DETECTION_ENABLED = True
    BEHAVIOR_ANOMALY_THRESHOLD = 0.5  # Score threshold for anomaly detection
    
    # Context-Aware Moderation
    CONTEXT_AWARE_MODERATION_ENABLED = True
    CONTEXT_SCORE_REDUCTION_MAX = 0.4  # Maximum spam score reduction from context
    
    # Adaptive Thresholds
    ADAPTIVE_THRESHOLDS_ENABLED = True
    ADAPTIVE_THRESHOLDS_MIN_SAMPLES = 10  # Minimum admin actions before learning
    ADAPTIVE_THRESHOLDS_ADJUSTMENT_RATE = 0.05  # How much to adjust thresholds per correction
