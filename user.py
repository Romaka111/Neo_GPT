from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field
from constants import SubscriptionType

class MemoryEntry(BaseModel):
    role: str  # "user" или "assistant"
    content: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
  
class User(BaseModel):
    telegram_id: int
    subscription: SubscriptionType = SubscriptionType.BASE
    subscription_start: Optional[datetime] = None
    subscription_end: Optional[datetime] = None
  
    used_messages_today: int = 0
    used_images_today: int = 0
    last_reset: datetime = Field(default_factory=datetime.utcnow)

    memory: List[MemoryEntry] = Field(default_factory=list)
    is_active: bool = True

    def reset_daily_limits(self):
        self.used_messages_today = 0
        self.used_images_today = 0
        self.last_reset = datetime.utcnow()
