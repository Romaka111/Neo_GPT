from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message(lambda msg: msg.text == "/start")
async def start_handler(message: Message):
    await message.answer("Привет! Я GPT-бот. Чем могу помочь?")