from handlers import setup_handlers
from config import TELEGRAM_TOKEN, BASE_URL
from aiogram import Bot, Dispatcher
import asyncio

async def main():
    print(f"TELEGRAM_TOKEN: {TELEGRAM_TOKEN} (type: {type(TELEGRAM_TOKEN)})") # отладка

    if not isinstance(TELEGRAM_TOKEN, str) or not TELEGRAM_TOKEN:
        raise ValueError("❌ TELEGRAM_TOKEN is not set or is not a string")
        
    bot = Bot(token=TELEGRAM_TOKEN)
    dp = Dispatcher()
    setup_handlers(dp)
    await bot.set_webhook(url=BASE_URL + "/webhook")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
