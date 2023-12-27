from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram import F

import app.keyboards as kb
from app.database.requests import get_products

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
    await callback.answer('Товары по выбранной категории: ', reply_markup=await kb.products(category_id))
    await callback.answer('')


@router.callback_query(F.data.startswish('product_'))
async def product_selected(callback: CallbackQuery):
    product_id = callback.data.split('_')[1]
    product = await get_products(product_id=product_id)
    await callback.answer(f'<b>{product.name}</b>\n\n{product.description}\n\n{product.price} руб.')
    await callback.answer(f'Вы выбрали {product.name}')


