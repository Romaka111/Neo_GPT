from aiogram import Router, types, F
from app.services.user_manager import get_or_create_user, increment_message_count
from app.services.openai_client import chat_with_gpt
from app.utils.subscriptions import check_subscription_limits

router = Router()

@router.message(F.text)
async def gpt_chat_handler(message: types.Message):
    user = await get_or_create_user(message.from_user)

    # Проверка лимитов
    if not check_subscription_limits(user):
        await message.answer("⚠️ Вы исчерпали лимит сообщений по вашей подписке.\nИспользуйте /buy для продления.")
        return

    await message.chat.do("typing")

    try:
        response = await chat_with_gpt(user_id=user['user_id'], message_text=message.text)
        await message.answer(response)

        # Обновление лимитов
        await increment_message_count(user['user_id'])
    except Exception as e:
        await message.answer("❌ Произошла ошибка при обращении к GPT. Попробуйте позже.")
        print(f"GPT error: {e}")
