from enum import Enum
from datetime import timedelta

class SubscriptionType(str, Enum):
    BASE = "base"
    STUDENT_PRO = "student_pro"
    SMART_PLUS = "smart_plus"
    ULTRA = "ultra"

SUBSCRIPTION_DETAILS = {
    SubscriptionType.BASE: {
        "name": "🔓 Base",
        "price": 0,
        "duration": None,  # бессрочно
        "gpt_model": "gpt-4o",
        "daily_message_limit": 10,
        "image_limit_per_day": 0,
        "priority": "low",
        "memory_limit": 5,
        "watermark": True,
    },
    SubscriptionType.STUDENT_PRO: {
        "name": "🌟 Student Pro",
        "price": 49,
        "duration": timedelta(days=1),
        "gpt_model": "gpt-4o",
        "daily_message_limit": None,
        "image_limit_per_day": 5,
        "priority": "medium",
        "memory_limit": 20,
        "watermark": False,
    },
    SubscriptionType.SMART_PLUS: {
        "name": "🚀 Smart+",
        "price": 149,
        "duration": timedelta(days=7),
        "gpt_model": "gpt-4o",
        "daily_message_limit": None,
        "image_limit_per_day": 5,
        "priority": "high",
        "memory_limit": 50,
        "watermark": False,
    },
    SubscriptionType.ULTRA: {
        "name": "👑 Ultra",
        "price": 349,
        "duration": timedelta(days=30),
        "gpt_model": "gpt-4o",
        "daily_message_limit": None,
        "image_limit_per_day": 5,
        "priority": "max",
        "memory_limit": 100,
        "watermark": False,
    },
}
