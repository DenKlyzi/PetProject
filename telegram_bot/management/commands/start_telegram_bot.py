import asyncio
import logging
from django.core.management import BaseCommand
from telegram_bot.bot import bot, dispatcher


logger = logging.getLogger('django')

class Command(BaseCommand):
    def handle(self, *args, **options):
        logger.info('BOT successfully started')
        asyncio.run(dispatcher.start_polling(bot))
