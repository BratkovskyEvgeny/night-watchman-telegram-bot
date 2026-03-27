FROM python:3.10-slim

# Устанавливаем системные зависимости для сборки некоторых пакетов
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем Python-зависимости без кэша
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код
COPY . .

# Запускаем бота
CMD ["python", "night_watchman.py"]
