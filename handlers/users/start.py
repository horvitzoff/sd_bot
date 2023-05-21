from loader import dp
from aiogram import types
from keyboards import keyboard

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет, Я бот для генераций изображений с помощью StableDiffusion.\nЧтобы я приступил к генерации нажми на кнопку ниже.', reply_markup=keyboard)
    