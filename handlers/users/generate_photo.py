from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from state import ResponseGenerate
from utils.sd_response import response_generate
from PIL import Image

def get_image_resolution(image_bytes):
    # Создаем объект Image из данных в объекте io.BytesIO
    image = Image.open(image_bytes)
    
    # Получаем разрешение (ширину и высоту) фото
    width, height = image.size
    
    # Возвращаем разрешение
    return width, height

@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def generate(message: types.Message):
    await message.answer("Пришлите фото")
    await ResponseGenerate.image.set()

@dp.message_handler(content_types=types.ContentTypes.PHOTO, state=ResponseGenerate.image)
async def process_image(message: types.Message, state: FSMContext):
    photo_id = message.photo[-1].file_id
    await state.update_data(photo_id=photo_id)
    await message.reply("Введите текст")
    await ResponseGenerate.text.set()

@dp.message_handler(content_types=types.ContentTypes.TEXT, state=ResponseGenerate.text)
async def process_text(message: types.Message, state: FSMContext):
    # Обработка текста
    text = message.text
    data = await state.get_data()
    photo_id = data.get("photo_id")
    # Далее можно использовать photo_id и text по своему усмотрению
    photo_file = await dp.bot.get_file(photo_id)
    downloaded_photo = await dp.bot.download_file(photo_file.file_path)
    wight, height = get_image_resolution(downloaded_photo)
    if (wight * height) > 500000:
        await message.answer("Изображение не сгенерированно, попробуйте понизить разрешение.")
    else:
        await message.answer("Генерирую изображение")
        image = response_generate(text, downloaded_photo, wight, height)
        await message.answer_photo(image)
    await state.finish()