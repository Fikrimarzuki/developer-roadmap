from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field


class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(index=True, foreign_key="user.id")
    status: str = "pending"  # pending / paid / cancelled
    created_at: datetime = Field(default_factory=datetime.utcnow)
