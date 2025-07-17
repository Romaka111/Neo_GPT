# main.py

from fastapi import FastAPI, Request
from aiogram import Bot, Dispatcher
from aiogram.types import Update
from aiogram.fsm.storage.memory import MemoryStorage
from commands import register_command_handlers
from message import register_message_handlers
from config import TELEGRAM_TOKEN, BASE_URL
import yoomoney

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
  print("Webhook установлен")

@app.post("/webhook")
async def telegram_webhook(request: Request):
  data = await request.json()
  update = Update(**data)
  await dp.feed_update(bot, update)
  return {"ok": True}

