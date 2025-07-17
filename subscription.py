from datetime import datetime, timedelta
from user import User
from constants import SubscriptionType, SUBSCRIPTION_DETAILS

def is_subscription_active(user: User) -> bool:
    return user.subscription_type != SubscriptionType.BASE and user.subscription_expires_at and user.subscription_expires_at > datetime.utcnow()

def get_subscription_config(user: User) -> dict:
    """Получить конфигурацию подписки"""
    return SUBSCRIPTION_DETAILS.get(user.subscription_type, SUBSCRIPTION_DETAILS[SubscriptionType.BASE])

def activate_subscription(user: User, sub_type: SubscriptionType):
    config = SUBSCRIPTION_DETAILS[sub_type]
    user.subscription_type = sub_type
    user.subscription_expires_at = datetime.utcnow() + timedelta(days=config["duration_days"])
    user.daily_message_limit = config["daily_limit"]
    user.images_left = config["image_limit"]
    user.updated_at = datetime.utcnow()

def expire_subscription(user: User):
    user.subscription_type = SubscriptionType.BASE
    user.subscription_expires_at = None
    user.daily_message_limit = SUBSCRIPTION_DETAILS[SubscriptionType.BASE]["daily_limit"]
    user.images_left = 0
    user.updated_at = datetime.utcnow()
    
def check_subscription_limits(user: User):
    """Проверка лимита сообщений"""
    subscription = SUBSCRIPTION_DETAILS[user.subscription_type]
    if subscription["daily_message_limit"] is not None:
        if user.daily_message_count >= subscription["daily_message_limit"]:
            return False, "🔒 Лимит сообщений на сегодня исчерпан. Приобретите подписку, чтобы продолжить."
    return True, None
