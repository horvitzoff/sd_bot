from aiogram.dispatcher.filters.state import State, StatesGroup

class ResponseGenerate(StatesGroup):
    image = State()
    text = State()