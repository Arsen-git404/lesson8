import os

BASE_URL = os.getenv("YOUGILE_BASE_URL", "https://ru.yougile.com/data/api-v1")
API_TOKEN = os.getenv("YOUGILE_TOKEN")  # Твой YOUGILE-KEY ключ
REQUEST_TIMEOUT = 10
