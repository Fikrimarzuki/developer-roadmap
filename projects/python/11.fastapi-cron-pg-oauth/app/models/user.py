from typing import Optional
from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True)
    name: str
    password_hash: Optional[str] = None
    role: str = "user"
    is_active: bool = True

    # OAuth-related
    google_id: Optional[str] = Field(default=None, index=True)
