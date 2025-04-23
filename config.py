import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

GOOGLE_SHEET_CREDENTIALS = "credentials.json"

GOOGLE_SHEET_NAME = "Таблица Вопрос-ответ"

WILDBERRIES_QUESTIONS_LINK = "https://example.com/questions"
WILDBERRIES_REVIEWS_LINK = "https://example.com/reviews"

