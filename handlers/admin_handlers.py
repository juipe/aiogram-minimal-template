from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
import logging

#importing admin_id
from config import ADMIN_ID

#importing database scripts
from data.database import get_total_users_count

admin_router = Router()

#users handler
@admin_router.message(Command("users"))
async def admin_stats_handler(message: Message):
    if message.from_user.id == ADMIN_ID:
        try:
            total_users_count = await get_total_users_count()
            await message.answer(f"Total users count: {total_users_count}")
        except Exception as e:
            logging.error(f"error in admin handler: {e}")
            await message.answer("error, try again later")