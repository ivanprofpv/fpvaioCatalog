from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram import F
from aiogram import html

from app import keyboards
from app.database.requests import get_products, get_product

router = Router()


@router.message(CommandStart())
async def handler_start(message: Message):
    await message.answer(f'Привет, {html.quote(message.from_user.full_name)}!', reply_markup=keyboards.main)


@router.message(F.text == "Каталог")
async def catalog(message: Message):
    await message.answer('Выберите вариант из каталога', reply_markup=await keyboards.categories())


@router.callback_query(F.data.startswith('category_'))
async def category_selected(callback: CallbackQuery):
    category_id = callback.data.split('_')[1]
    await callback.message.answer('Товары по выбранной категории: ', reply_markup=await keyboards.products(category_id))
    await callback.answer('')


@router.callback_query(F.data.startswith('product_'))
async def product_selected(callback: CallbackQuery):
    product_id = callback.data.split('_')[1]
    product = await get_product(product_id=product_id)
    await callback.message.answer(f'<b>{product.name}</b>\n\n{product.description}\n\n{product.price} руб.')
    await callback.answer('')


