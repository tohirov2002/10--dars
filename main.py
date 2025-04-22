from aiogram import Bot,Dispatcher
import logging
import asyncio
import sys

dp = Dispatcher()

from config import BOT_TOKEN
from handlers.start_handler import start_router
from handlers.add_task import add_router
from database.db import init_db

async def main():
    print("Botim ishga tushdi....")
    init_db()
    bot = Bot(token=BOT_TOKEN)
    dp.include_router(add_router)
    dp.include_router(start_router)
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Bot stopped")
