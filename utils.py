import logging
import re
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from aiogram import types
from config import GOOGLE_SHEET_CREDENTIALS, GOOGLE_SHEET_NAME, WILDBERRIES_QUESTIONS_LINK, WILDBERRIES_REVIEWS_LINK
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pymorphy3 import MorphAnalyzer
from nltk.corpus import stopwords
import nltk


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Автоматическая загрузка стоп-слов NLTK, если они отсутствуют
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    logger.info("Загрузка стоп-слов NLTK...")
    nltk.download('stopwords')

morph = MorphAnalyzer()
stop_words = set(stopwords.words('russian'))


def get_google_sheet():
    """
    Получение данных из Google Sheets.
    Возвращает объект листа Google Sheets.
    """
    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name(GOOGLE_SHEET_CREDENTIALS, scope)
        client = gspread.authorize(creds)
        sheet = client.open(GOOGLE_SHEET_NAME).sheet1
        return sheet
    except Exception as e:
        logger.error(f"Ошибка при получении Google Sheet: {e}")
        raise


def lemmatize_text(text):
    """
    Лемматизация текста: приведение слов к нормальной форме и удаление стоп-слов.
    Аргументы:
        text (str): Входной текст.
    Возвращает:
        list: Список лемматизированных слов.
    """
    words = re.findall(r'\w+', text.lower())
    lemmas = [morph.parse(word)[0].normal_form for word in words if word not in stop_words]
    return lemmas


def find_answer(question):
    """
    Поиск ответа на вопрос пользователя с использованием TF-IDF и косинусного сходства.
    Аргументы:
        question (str): Вопрос пользователя.
    Возвращает:
        str or None: Ответ из Google Sheets или None, если подходящий ответ не найден.
    """
    try:
        # Получение данных из Google Sheets
        sheet = get_google_sheet()
        data = sheet.get_all_records()
        questions = [row['Вопрос'] for row in data]
        
        # Преобразование вопросов в TF-IDF векторы
        vectorizer = TfidfVectorizer(tokenizer=lemmatize_text)
        tfidf_matrix = vectorizer.fit_transform(questions)
        user_question_vec = vectorizer.transform([question])
        
        # Вычисление косинусного сходства
        similarities = cosine_similarity(user_question_vec, tfidf_matrix).flatten()
        best_match_idx = similarities.argmax()
        threshold = 0.2  # Порог для минимального сходства (можно настроить)
        
        # Проверка, превышает ли сходство порог
        if similarities[best_match_idx] > threshold:
            return data[best_match_idx]['ОТВЕТ']
        else:
            return None
    except Exception as e:
        logger.error(f"Ошибка при поиске ответа: {e}")
        return None


async def handle_question(message: types.Message):
    """
    Обработка вопроса пользователя в Telegram-боте.
    Аргументы:
        message (types.Message): Сообщение от пользователя.
    """
    question = message.text
    answer = find_answer(question)
    
    if answer:
        await message.answer(answer)
    else:
        await message.answer(
            f"К сожалению, у меня нет точной информации о '{question}'. "
            "Вы можете ознакомиться с вопросами, а также задать Ваш вопрос о нашем продукте на WILDBERRIES по следующим ссылкам: "
            f"[Вопросы на WILDBERRIES]({WILDBERRIES_QUESTIONS_LINK}) и [Отзывы на WILDBERRIES]({WILDBERRIES_REVIEWS_LINK})"
        )