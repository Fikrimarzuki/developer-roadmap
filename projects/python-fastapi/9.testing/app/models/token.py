from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field

class RefreshToken(SQLModel, table=True):
  id: Optional[int] = Field(default=None, primary_key=True)
  user_id: int = Field(index=True)
  token: str = Field(unique=True, index=True)
  expires_at: datetime
  revoked: bool = False
