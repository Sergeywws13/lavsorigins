import asyncio
from aiogram import Bot, Dispatcher
from config import TELEGRAM_BOT_TOKEN
from handlers.start import start_router
from handlers.callback_router import callback_router
from handlers.question_router import question_router
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    dp = Dispatcher(bot=bot)

    dp.include_router(start_router)
    dp.include_router(question_router)
    dp.include_router(callback_router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
