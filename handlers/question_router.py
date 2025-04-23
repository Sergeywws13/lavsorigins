import logging
from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils import find_answer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

question_router = Router()

class QuestionStates(StatesGroup):
    waiting_for_question = State()

@question_router.callback_query(lambda query: query.data == "question")
async def question_callback(query: types.CallbackQuery, state: FSMContext):
    await query.answer()
    text = """
    Задайте ваш вопрос о нашем продукте, и мы постараемся ответить вам в ближайшее время.
    """
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Назад", callback_data="start")]
        ]
    )
    await query.message.answer(text, reply_markup=keyboard)
    
    await state.set_state(QuestionStates.waiting_for_question)

@question_router.message(QuestionStates.waiting_for_question)
async def handle_question(message: types.Message, state: FSMContext):
    logger.info(f"Получен вопрос: {message.text}")
    question = message.text
    answer = find_answer(question)

    if answer:
        await message.answer(answer)
    else:
        await message.answer(
            f"К сожалению, у меня нет точной информации о '{question}'. Вы можете ознакомиться с вопросами, а также задать Ваш вопрос о нашем продукте на WILDBERRIES по следующим ссылкам: "
            f"[Вопросы на WILDBERRIES](https://example.com/questions) и [Отзывы на WILDBERRIES](https://example.com/reviews)"
        )
    
    await state.clear()