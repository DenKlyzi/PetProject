import logging

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from telegram_bot import messages


logger = logging.getLogger('django')
start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: Message):
    user_info = message.from_user
    await message.answer(messages.WELCOME_MESSAGE)
