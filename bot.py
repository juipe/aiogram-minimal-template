import asyncio
import logging

#Importing data
from config import BOT_TOKEN

#Aiogram moduls
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

#Importing routers
from handlers.user_handlers import user_router
from handlers.admin_handlers import admin_router

#Database init
from data.database import init_database

logging.basicConfig(level=logging.INFO)
dp = Dispatcher()

#Launch the bot
async def main():
    #including routers
    dp.include_router(user_router)
    dp.include_router(admin_router)

    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await init_database() #Initializing the database
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("stopped by user")