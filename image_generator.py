import os
import uuid
from PIL import Image, ImageDraw, ImageFont
from app.core.openai_client import openai_image
from app.services.user_manager import increment_user_image_usage
from app.utils.subscriptions import has_active_subscription, get_image_limit
from app.constants import TEMP_IMAGE_DIR

# Убедимся, что папка для временных изображений существует
os.makedirs(TEMP_IMAGE_DIR, exist_ok=True)

WATERMARK_TEXT = "NeoGPT Preview"
WATERMARK_FONT_SIZE = 24

async def generate_image_with_access_check(user: dict, prompt: str):
    image_limit = get_image_limit(user)
    used = user.get("image_usage", 0)

    is_subscribed = has_active_subscription(user)
    is_preview = not is_subscribed or (used >= image_limit)

    # Генерация изображения
    image_url = await openai_image(prompt)

    filename = f"{uuid.uuid4().hex}.jpg"
    filepath = os.path.join(TEMP_IMAGE_DIR, filename)

    # Загрузка и сохранение изображения
    import requests
    response = requests.get(image_url)
    with open(filepath, "wb") as f:
        f.write(response.content)

    # Добавление водяного знака при необходимости
    if is_preview:
        add_watermark(filepath)

    if not is_preview:
        await increment_user_image_usage(user["_id"])

    return filepath, is_preview

def add_watermark(filepath: str):
    image = Image.open(filepath).convert("RGBA")
    width, height = image.size

    watermark = Image.new("RGBA", image.size)
    draw = ImageDraw.Draw(watermark)

    try:
        font = ImageFont.truetype("arial.ttf", WATERMARK_FONT_SIZE)
    except:
        font = ImageFont.load_default()

    text_width, text_height = draw.textsize(WATERMARK_TEXT, font)
    position = (width - text_width - 10, height - text_height - 10)

    draw.text(position, WATERMARK_TEXT, fill=(255, 255, 255, 128), font=font)
    watermarked = Image.alpha_composite(image, watermark)
    watermarked.convert("RGB").save(filepath, "JPEG")
