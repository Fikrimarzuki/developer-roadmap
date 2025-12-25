from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(index=True, foreign_key="user.id")
    status: str = "pending"
    created_at: datetime = Field(default_factory=datetime.utcnow)
