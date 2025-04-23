from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile

start_router = Router()

@start_router.message(Command("start"))
async def start_command(message: Message):
    text = """
🌟 Добрый день! 🌟

Используйте кнопки меню ниже. С удовольствием помогу вам!
    """
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📜 Описание устройства", callback_data="description")],
            [InlineKeyboardButton(text="✨ Эффект", callback_data="effect")],
            [InlineKeyboardButton(text="🎯 Способ применения", callback_data="use")],
            [InlineKeyboardButton(text="💄 Рекомендации косметика-эстетиста", callback_data="expert_recommendations")],
            [InlineKeyboardButton(text="🤔 Задать вопрос?", callback_data="question")],
            [InlineKeyboardButton(text="📝 Гарантийные обязательства/Брак продукции", callback_data="garant")],
        ]
    )
    await message.answer_photo(
        photo=FSInputFile("images/1.png", filename="LAVSORIGINS.jpg"),
        caption=text,
        reply_markup=keyboard
    )