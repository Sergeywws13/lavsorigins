from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile

start_router = Router()

@start_router.message(Command("start"))
async def start_command(message: Message):
    text = """
🌟 Добро пожаловать в Умный чат-бот LAVSORIGINS! 🌟

Я здесь, чтобы раскрыть секреты красоты и здоровья вашей кожи с помощью нашего инновационного устройства.

✨ Узнайте, как повседневный уход за кожей может стать идеальным ритуалом красоты.

Начните ваше путешествие к совершенству уже сегодня!
"""
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Описание устройства", callback_data="description")],
            [InlineKeyboardButton(text="Эффект", callback_data="effect")],
            [InlineKeyboardButton(text="Способ применения", callback_data="use")],
            [InlineKeyboardButton(text="Задать вопрос?", callback_data="question")],
            [InlineKeyboardButton(text="Гарантийные обязательства/Брак продукции", callback_data="garant")],
        ]
    )
    
    await message.answer_photo(
        photo=FSInputFile("images/photo_2025-04-14_20-15-21.jpg", filename="LAVSORIGINS.jpg"),
        caption=text,
        reply_markup=keyboard
    )

