import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Путь к JSON-файлу с учетными данными
GOOGLE_SHEET_CREDENTIALS = "credentials.json"

# Имя Google Sheets
GOOGLE_SHEET_NAME = "Таблица Вопрос-ответ"

# Ссылки на WILDBERRIES
WILDBERRIES_QUESTIONS_LINK = "https://example.com/questions"
WILDBERRIES_REVIEWS_LINK = "https://example.com/reviews"

