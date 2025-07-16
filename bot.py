from handlers import setup_handlers
from config import TELEGRAM_TOKEN, BASE_URL
from aiogram import Bot, Dispatcher
import asyncio

async def main():
    bot = Bot(token=TELEGRAM_TOKEN)
    dp = Dispatcher()
    setup_handlers(dp)
    await bot.set_webhook(url=BASE_URL + "/webhook")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())