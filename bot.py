import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import BOT_TOKEN

# Включаем логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Инициализация бота
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
  await meesage.answer("Привет! Я бот GPT ✨")

async def on_startup(_):
  logger.info("✅ Бот успешно запущен и готов к работе.")

async def main():
  try:
    logger.info("🔄 Иницализация бота...")
        await dp.start_polling()
    except Exception as e:
        logger.error(f"❌ Ошибка при запуске бота: {e}")

if __name__ == '__main__':
    logger.info("🚀 Старт скрипта bot.py")
    asyncio.run(main())
