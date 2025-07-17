import openai
from constants import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

async def openai_chat(messages: list, model: str = "gpt-4o"):
    try:
        response = await openai.ChatCompletion.acreate(
            model=model,
            messages=messages,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Ошибка OpenAI: {str(e)}"

async def openai_image(prompt: str) -> str:
    try:
        response = await openai.Image.acreate(
            prompt=prompt,
            n=1,
            size="1024x1024",
            response_format="url"
        )
        return response["data"][0]["url"]
    except Exception as e:
        raise RuntimeError(f"Ошибка при генерации изображения: {str(e)}")
