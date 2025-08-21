import logging

from aiogram import Router
from aiogram.types import Message
from telegram_bot.services.neuron_model_service import NeuronModelService
from telegram_bot.bot import Bot

logger = logging.getLogger('django')
message_router = Router()


@message_router.message()
async def handle_user_message(message: Message, bot: Bot):
    bot_message = await message.reply("⏳ Ваш вопрос принят. Обрабатываю...")
    response_text = NeuronModelService.get_ai_response(
        prompt=message.text,
        user_id=message.from_user.id,
    )
    await bot.delete_message(chat_id=message.from_user.id, message_id=bot_message.message_id)
    await message.reply(response_text)
