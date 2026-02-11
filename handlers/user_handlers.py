from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
import logging

#import create user func
from data.database import create_user

#import main_keyboard
from keyboards.main_keyboard import get_main_keyboard

user_router = Router()

#Start handler
@user_router.message(Command("start"))
async def command_start_handler(message: Message):
    try:
        userid = message.from_user.id
        username = message.from_user.username
        userdata = [userid, username]
        await create_user(userdata)

        await message.answer("<b>start message</b>", reply_markup=get_main_keyboard())
    except Exception as e:
        logging.error(f"error in start handler: {e}")
        await message.answer("error, try again later")

#Help handler
@user_router.message(Command("help"))
async def command_help_handler(message: Message):
    await message.answer("/start - start message\n/help - help message")

#Help handler with text
@user_router.message(F.text == "Help")
async def command_help_handler(message: Message):
    await message.answer("/start - start message\n/help - help message")