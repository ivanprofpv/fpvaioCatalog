from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
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
async def category_selected(callback: CallbackQuery):
    category_id = callback.data.split('_')[1]
    await callback.answer(f'Вы выбрали категорию {category_id}')
    await callback.answer('Категория выбрана!')


