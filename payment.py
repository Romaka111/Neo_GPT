# app/core/payment.py

import hashlib
from datetime import datetime, timedelta
from app.utils.user_manager import set_subscription

# Токен ЮMoney (из переменной окружения)
import os
YOOMONEY_SECRET = os.getenv("YOOMONEY_SECRET", "")

# Подписки: название -> (срок_дней, уровень)
SUBSCRIPTION_PLANS = {
    "Student Pro": (1, "student_pro"),
    "Smart+": (7, "smart_plus"),
    "Ultra": (30, "ultra")
}

def verify_signature(data: dict) -> bool:
    """
    Проверяет подпись ЮMoney по данным запроса.
    """
    string = "&".join([
        data.get("notification_type", ""),
        data.get("operation_id", ""),
        data.get("amount", ""),
        data.get("currency", ""),
        data.get("datetime", ""),
        data.get("sender", ""),
        data.get("codepro", ""),
        YOOMONEY_SECRET,
        data.get("label", "")
    ])
    sha1 = hashlib.sha1(string.encode("utf-8")).hexdigest()
    return sha1 == data.get("sha1_hash", "")

async def process_payment(data: dict):
    """
    Обрабатывает успешный платёж.
    """
    if not verify_signature(data):
        raise ValueError("Неверная подпись платежа")

    label = data.get("label")  # Telegram user_id
    amount = float(data.get("amount", 0))

    # Определим подписку по сумме
    plan = None
    for name, (days, level) in SUBSCRIPTION_PLANS.items():
        if (name == "Student Pro" and amount >= 49) or \
           (name == "Smart+" and amount >= 149) or \
           (name == "Ultra" and amount >= 349):
           plan =  days, level)
            break

    if not plan:
        raise ValueError("Неизвестный тариф")

    days, level = plan
    expires = datetime.utcnow() + timedelta(days=days)
    await set_subscription(label, level, expires)
