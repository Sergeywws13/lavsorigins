import gspread
from oauth2client.service_account import ServiceAccountCredentials
from aiogram import types
from config import GOOGLE_SHEET_CREDENTIALS, GOOGLE_SHEET_NAME, WILDBERRIES_QUESTIONS_LINK, WILDBERRIES_REVIEWS_LINK

# Настройка доступа к Google Sheets
def get_google_sheet():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(GOOGLE_SHEET_CREDENTIALS, scope)
    client = gspread.authorize(creds)
    sheet = client.open(GOOGLE_SHEET_NAME).sheet1  # Открываем первый лист
    return sheet

# Функция для поиска ответа на вопрос
def find_answer(question):
    sheet = get_google_sheet()
    data = sheet.get_all_records()  # Получаем все данные из таблицы

    for row in data:
        if question.lower() in row['Вопрос'].lower():
            return row['ОТВЕТ']
    return None

async def handle_question(message: types.Message):
    question = message.text
    answer = find_answer(question)

    if answer:
        await message.answer(answer)
    else:
        await message.answer(
            f"К сожалению, у меня нет точной информации о '{question}'. Вы можете ознакомиться с вопросами, а также задать Ваш вопрос о нашем продукте на WILDBERRIES по следующим ссылкам: "
            f"[Вопросы на WILDBERRIES]({WILDBERRIES_QUESTIONS_LINK}) и [Отзывы на WILDBERRIES]({WILDBERRIES_REVIEWS_LINK})"
        )
