import asyncio
import logging

from typing import Any
from django.core.management import BaseCommand
from telegram_bot.bot import bot, dispatcher

logger = logging.getLogger('django')


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> None:
        logger.info('BOT successfully started')
        asyncio.get_event_loop().run_until_complete(dispatcher.start_polling(bot))
