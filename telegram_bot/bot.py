from django.conf import settings
import logging
from aiogram import Bot, Dispatcher

logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.BOT_API_KEY)
dispatcher = Dispatcher()
