from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

#main keyboard
def get_main_keyboard():
    keyboard = [
        [KeyboardButton(text="Help")],
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)