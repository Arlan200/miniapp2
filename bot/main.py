import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from aiogram.filters import Command
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBAPP_URL = os.getenv("WEBAPP_URL")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    webapp_button = KeyboardButton(
        text="Открыть WebApp",
        web_app=WebAppInfo(url=WEBAPP_URL)
    )

    keyboard = ReplyKeyboardMarkup(
        keyboard=[[webapp_button]],
        resize_keyboard=True,
        one_time_keyboard=True
    )

    await message.answer(
        "Привет! Нажми на кнопку ниже, чтобы открыть WebApp:",
        reply_markup=keyboard
    )

async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
