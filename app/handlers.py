from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from magic_filter import F

import app.keyboards as kb

router = Router()


@router.message(CommandStart())
async def handler_start(message: Message):
    await message.answer(f'Привет, {message.from_user.full_name}!', reply_markup=kb.main)


@router.message(F.text=="Каталог")
async def catalog(message: Message):
    await message.answer('Выберите вариант из каталога', reply_markup=await kb.categories())

@router.callback_query(F.data.startswish('category_'))
async def category_selected(message: Message):
    category_id = message.data.split('_')[1]
    await message.answer(f'Вы выбрали категорию {category_id}')


