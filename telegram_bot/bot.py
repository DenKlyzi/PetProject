import logging
from aiogram import Bot, Dispatcher
from telegram_bot.handlers.start import start_router
from telegram_bot.handlers.api_messager import message_router
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from django.conf import settings


logging.basicConfig(level=logging.DEBUG)

bot = Bot(
    token=settings.BOT_API_KEY,
    default=DefaultBotProperties(parse_mode='HTML')
)

dispatcher = Dispatcher(storage=MemoryStorage())
dispatcher.include_router(start_router)
dispatcher.include_router(message_router)
