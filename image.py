from aiogram import Router, types
from aiogram.filters import Command
from app.services.user_manager import get_or_create_user
from app.services.image_generator import generate_image_with_access_check

router = Router()

@router.message(Command("image"))
async def handle_image_command(message: types.Message):
    user = await get_or_create_user(message.from_user)

    prompt = message.text.replace("/image", "").strip()
    if not prompt:
        await message.answer("🖼 Пожалуйста, введите описание изображения после команды:\n\n`/image кот в шляпе`", parse_mode="Markdown")
        return

    await message.chat.do("upload_photo")

    try:
        image_file, is_preview = await generate_image_with_access_check(user, prompt)

        await message.answer_photo(
            types.FSInputFile(image_file),
            caption="🖼 Превью изображения с водяным знаком" if is_preview else "✅ Сгенерировано по вашему описанию"
        )
    except Exception as e:
        await message.answer("❌ Ошибка генерации изображения. Попробуйте позже.")
        print(f"Image generation error: {e}")
