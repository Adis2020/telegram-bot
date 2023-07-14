import os
import pytesseract
from PIL import Image
from datetime import date, datetime
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from functions import getTime

load_dotenv()

TOKEN = os.getenv("TOKEN")
custom_config = os.getenv("CUSTOM_CONFIG")

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=["start"])
async def start(msg: types.Message):
    await msg.answer("Добро пожаловать! Пришлите своё фото и я обработую его и пришлю в цифровом варианте.\n"
                     "Данный бот пока что распознают текста только на английском.\n"
                     "ВНИМАНИЕ!\n"
                     "Для корректного разпознания текста от пользователя требуется повысить некоторые параметры в изображении!\n"
                     "А именно контрастность и чёткость! Также можно изменять другие параметры если вам покажется что чёткость изображения повысится")


@dp.message_handler(commands=["help"])
async def help(msg: types.Message):
    await msg.answer("Доступные вам команды: \n/start \n/help \n/moreInfo")


@dp.message_handler(commands=["moreInfo"])
async def info(msg: types.Message):
    await msg.answer("Если вы обнаружили проблемы некорретной разпознование текста то пишите сюда: @Adis223\n"
                     "Ошибки которые на данный момент известно:\n"
                     "Заглавная буква I. Если вы вдруг в тексте использутся шрифт то каждая буква должна различатся между собой!")


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def get_photo(msg: types.Message):
    photo_id = msg.photo[-1].file_id

    minute = getTime(datetime.now().minute)
    hour = getTime(datetime.now().hour)
    day = getTime(date.today().day)
    month = getTime(date.today().month)
    year = getTime(date.today().year)

    photo_file = await bot.get_file(photo_id)
    save_path = 'users_images'
    save_file_path = os.path.join(save_path, f'{year}-{month}-{day}_{hour}.{minute}({msg.from_user.id}).jpg')
    await photo_file.download(destination_file=save_file_path)

    await msg.answer(pytesseract.image_to_string(Image.open(save_file_path), config=custom_config))


if __name__ == '__main__':
    executor.start_polling(dp)