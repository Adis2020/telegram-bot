from aiogram.types import ReplyKeyboardMarkup, ContentType

start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
start_keyboard.add("Обо мне").add("Чем занимаюсь").add("Контакты")