from aiogram.utils.keyboard import KeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from services.timer import actualy_matches


start_button : KeyboardButton = KeyboardButton(text='Запуск')
start_keyboard : ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                keyboard=[[start_button]],resize_keyboard=True)
def create_time_info():
    buttons = []
    kb_builder : InlineKeyboardBuilder = InlineKeyboardBuilder()
    for button,text in actualy_matches.items():
        buttons.append(InlineKeyboardButton(text=button,
        callback_data=text))
    kb_builder.row(*buttons,width=1)
    return kb_builder.as_markup()
