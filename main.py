# main.py

from fastapi import FastAPI
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from commands import register_command_handlers
from message import register_message_handlers
from app.webhook import yoomoney
from config import TELEGRAM_TOKEN, BASE_URL

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(storage=MemoryStorage())
register_command_handlers(dp)
register_message_handlers(dp)

app = FastAPI()

# Подключаем маршруты ЮMoney
app.include_router(yoomoney.router)

@app.on_event("startup")
async def on_startup():
  await bot.set_webhook(f"{BASE_URL}/webhook")

# Подключаем Telegram webhook в FastAPI
setup_application(app, dp, bot=bot)
SimpleRequestHandler(dispatcher=dp, bot=bot).register(app, path="/webhook")
