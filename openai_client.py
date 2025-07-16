import os
import openai
from app.database.user_manager import get_subscription_config, add_to_memory
from app.database.models.user import User
from app.core.constants import SubscriptionType

openai.api_key = os.getenv("OPENAI_API_KEY")

async def generate_gpt_reply(user: User, prompt: str) -> str:
    config = get_subscription_config(user)
    model = config["model"]

    # Формируем историю (память)
    messages = [{"role": m.role, "content": m.content} for m in user.memory]
    messages.append({"role": "user", "content": prompt})

    try:
        response = await openai.ChatCompletion.acreate(
            model=model,
            messages=messages,
            temperature=0.7,
            max_tokens=1000
        )
        reply = response.choices[0].message.content.strip()

        # Обновляем память
        add_to_memory(user, "user", prompt)
        add_to_memory(user, "assistant", reply)

        return reply
    except Exception as e:
        return f"❌ Ошибка при генерации ответа: {e}"
