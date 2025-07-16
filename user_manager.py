from datetime import datetime, timedelta
from pymongo import MongoClient
from bson import ObjectId
from app.database.models.user import User, MemoryEntry
from app.core.constants import SUBSCRIPTION_CONFIG, SubscriptionType
import os

MONGO_URL = os.getenv("MONGO_URL")
client = MongoClient(MONGO_URL)
db = client["neogpt"]
users_collection = db["users"]

def get_user(telegram_id: int) -> User:
    data = users_collection.find_one({"telegram_id": telegram_id})
    if data:
        user = User(**data)
        # Сброс лимитов, если день прошёл
        if user.last_reset.date() != datetime.utcnow().date():
            user.reset_daily_limits()
        save_user(user)
        return user
        
    new_user = User(telegram_id=telegram_id)
    save_user(new_user)
    return new_user
    
def save_user(user: User):
    users_collection.update_one(
        {"telegram_id": user.telegram_id},
        {"$set": user.dict()},
        upsert=True
    )
    
def is_subscription_active(user: User) -> bool:
    if not user.subscription_end:
        return False
    return datetime.utcnow() < user.subscription_end

def get_subscription_config(user: User) -> dict:
    return SUBSCRIPTION_CONFIG.get(user.subscription, SUBSCRIPTION_CONFIG[SubscriptionType.BASE])

def increment_usage(user: User, message: bool = False, image: bool = False):
    if message:
        user.used_messages_today += 1
    if image:
        user.used_images_today += 1
    save_user(user)

def can_use_feature(user: User, feature: str) -> bool:
    config = get_subscription_config(user)
    if feature == "message":
        return user.used_messages_today < config["max_messages_per_day"]
    if feature == "image":
        return user.used_images_today < config["max_images_per_day"]
    return False

def add_to_memory(user: User, role: str, content: str):
    user.memory.append(MemoryEntry(role=role, content=content))
    if len(user.memory) > 20:
        user.memory.pop(0)  # ограничиваем длину памяти
    save_user(user)

def clear_memory(user: User):
    user.memory = []
    save_user(user)
