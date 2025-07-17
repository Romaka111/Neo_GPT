from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from user_manager import get_or_create_user
from subscription import is_subscription_active, get_subscription_config

router = Router()

@router.message(CommandStart())
async def start_handler(message: types.Message):
  user = await get_or_create_user(message.from_user)
  text = (
    f"👋 Привет, {message.from_user.first_name}!\n\n"
    "Я — NeoGPT, твой персональный AI-помощник в Telegram.\n"
    "Готов помочь тебе с учебой, бизнесом, аналитикой и многим другим.\n\n"
    "📌 Используй /help для списка команд.\n"
    "💼 Используй /profile, чтобы узнать свою подписку и лимиты."
  )
  await message.answer(text)
  
@router.message(Command("help"))
async def help_handler(message: types.Message):
  text = (
    "📖 Доступные команды:\n\n"
    "/start — Запуск бота\n"
    "/help — Помощь\n"
    "/profile — Текущая подписка и лимиты\n"
    "/buy — Купить/обновить подписку"
  )
  await message.answer(text)
  
  @router.message(Command("profile"))
  async def profile_handler(message: types.Message):
    user = await get_or_create_user(message.from_user)
    text = format_subscription_info(user)
    await message.answer(text)

def register_command_handlers(dispatcher):
    dispatcher.include_router(router)
