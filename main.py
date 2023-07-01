import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
from keyboard import start_keyboard

load_dotenv()

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=["start"])
async def start(msg: types.Message):
    await msg.answer("Добро пожаловать!", reply_markup=start_keyboard)


@dp.message_handler(commands=["help"])
async def start(msg: types.Message):
    await msg.answer("Доступные вам команды: \n/start \n/help")


@dp.message_handler(text="Обо мне")
async def about(msg: types.Message):
    await msg.reply("Меня зовут Адис")


@dp.message_handler(text="Чем занимаюсь")
async def about(msg: types.Message):
    await msg.reply("Занимаюсь я программированием.\n"
                    "Мне 15 лет и я владею навыкми React, HTML, CSS, JavaScript, Python и немного разбираюсь в работе GitHub :)\n"
                    "На данный момент учусь создавать ботов чтобы немного подзаработать")


@dp.message_handler(text="Контакты")
async def about(msg: types.Message):
    await msg.reply("Вы можете со мной связатся через telegram, watsapp, discord\n"
                    "Discord: adis223\n"
                    "Watsapp: 996-709-147-518\n"
                    "Telegram: 996-709-147-518\n")


if __name__ == '__main__':
    executor.start_polling(dp)
