import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.filters import Command

API_TOKEN = "7369112948:AAGnOqWpMr6KvAMH8S9VddWeQUekjv7I4yM"  # Вставьте ваш реальный токен
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)

# Создаем объект Dispatcher
dp = Dispatcher()

long_text = (
    "Добро пожаловать в Coconut Clicker!"
    "\nОсновные возможности в этой игре:"
    "\n• Кликайте на кокос, чтобы зарабатывать кокосы, и прокачивайтесь для большей эффективности!"
    "\n• Собирайте уникальные предметы, улучшайте свои скины и управляйте ресурсами."
    "\nСтаньте мастером кокосового бизнеса прямо сейчас, нажав на кнопку игры ниже!"
)


game_url = "https://t.me/CoconutClicker"  # Ссылка на вашего бота
web_app_url = "https://suspect147.github.io/CoconutClickerTelegram/"  # URL мини-игры
photo_url = "https://raw.githubusercontent.com/SusPect147/CoconutClickerTelegram/main/coconut_coconut.png"


@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    # Создаем клавиатуру
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Телеграм канал", url=game_url)],
            [InlineKeyboardButton(text="Тапни сюда для игры!", web_app=WebAppInfo(url=web_app_url))]
        ]
    )

    # Отправляем фото с описанием и клавиатурой
    await message.answer_photo(
        photo=photo_url,
        caption=long_text,
        reply_markup=keyboard
    )


async def main():
    logging.info("Starting bot...")
    # Запуск бота
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
