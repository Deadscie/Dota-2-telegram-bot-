from aiogram.utils.keyboard import KeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from services.timer import actualy_matches
from services.parser_liquipedia.parse_liquipedia import tournaments_dict


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
def create_kb_for_tournaments():
    buttons = []
    for i in tournaments_dict.keys():
        buttons.append([InlineKeyboardButton(text = i,
        callback_data=i)])
    kb = InlineKeyboardMarkup(inline_keyboard = buttons)
    return kb
def create_kb_for_info(tournament):
    buttons = []
    info_button = InlineKeyboardButton(text='Информация о туринире',callback_data='info')
    participants_button = InlineKeyboardButton(text='Команды на турнире',callback_data='participants')
    buttons.append([info_button])
    buttons.append([participants_button])
    kb = InlineKeyboardMarkup(inline_keyboard = buttons)
    return kb