from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button1 = KeyboardButton("Сгенерировать изображение")
keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(button1)