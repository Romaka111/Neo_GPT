from datetime import datetime
from typing import List
from pymongo.collection import Collection
from app.core.constants import MAX_MEMORY_MESSAGES

class MemoryStorage:
    def __init__(self, collection: Collection):
        self.collection = collection

    async def add_message(self, user_id: int, role: str, content: str):
        await self.collection.insert_one({
            "user_id": user_id,
            "role": role,
            "content": content,
            "timestamp": datetime.utcnow()
        })

    async def get_memory(self, user_id: int) -> List[dict]:
        cursor = self.collection.find({"user_id": user_id}).sort("timestamp", -1).limit(MAX_MEMORY_MESSAGES)
        messages = await cursor.to_list(length=MAX_MEMORY_MESSAGES)
        return list(reversed(messages))  # Вернём в хронологическом порядке

    async def clear_memory(self, user_id: int):
        await self.collection.delete_many({"user_id": user_id})
