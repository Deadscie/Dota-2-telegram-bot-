import requests
import asyncio
from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, Text, CommandStart
from lexicon.lexicon_ru import LEXICON
from services.converter import convert_mathes
from services.timer import timer
from services.parse_liquipedia import parse
from keyboards.keyboards import start_keyboard,create_time_info
from services.services import all_matches_message


router: Router = Router()

@router.message(CommandStart())
async def start_bot(message:Message):
    await message.answer(text=LEXICON['/start'])
    parse()
    convert_mathes()

@router.message(Command(commands='/help'))
async def help_bot(message:Message):
    await message.answer(LEXICON['/help'])

@router.message(Command(commands='all_mathes'))
async def all_mathes_bot(message:Message):
    await message.answer(all_matches_message())

@router.message(Command(commands='time_math'))
async def time_mathes_bot(message:Message):
    await message.answer('Выбери матч чтобы узнать через сколько он начнется',reply_markup=create_time_info())


@router.message(Command(commands='enable'))
async def timer_bot(message:Message):
    stop = False
    parse()
    await message.answer('Теперь я сообщу когда начнется матч')
    while True:
        await asyncio.sleep(0.1)
        time = timer()
        if time and not stop:
            await message.answer('Сейчас идем матч:  '+time+' беги смотреть')
            stop = True



@router.callback_query()
async def time_math(callback:CallbackQuery):
    if callback.data == callback.message.text:
        await callback.answer()
    else:
        await callback.message.edit_text(text=callback.data,reply_markup=callback.message.reply_markup)




@router.message()
async def enable_bot(message:Message):
    await message.answer(text= '1',reply_markup=start_keyboard)
