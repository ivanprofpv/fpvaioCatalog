import sys
import asyncio
import logging
import os

from aiogram import Bot, Dispatcher



async def main():
    bot = Bot(token=os.getenv('BOT_TOKEN'))
    dp = Dispatcher()

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot stopped')
