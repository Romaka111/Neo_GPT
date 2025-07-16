import motor.motor_asyncio
from app.core.constants import MONGO_URL

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
db = client["neogpt_bot"]

# Коллекции
users_collection = db["users"]
memory_collection = db["memory"]
payments_collection = db["payments"]
