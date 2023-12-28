import sys
import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from app import handlers
from app.database.models import async_main

load_dotenv()


async def main():
    await async_main()

    bot = Bot(token=os.getenv('BOT_TOKEN'), parse_mode='HTML')
    dp = Dispatcher()
    dp.include_router(handlers.router)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot stopped')
