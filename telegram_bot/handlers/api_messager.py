from aiogram import Router
from aiogram.types import Message


message_router = Router()

@message_router.message()
async def get_message(message: Message):
    await message.reply(f'Ваш вопрос принят. Сейчас найду ответ.')
