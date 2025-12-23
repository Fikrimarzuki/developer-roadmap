from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserRead(BaseModel):
  id: int
  email: EmailStr
  name: str
  role: str
  is_active: bool

class UserUpdate(BaseModel):
  email: Optional[EmailStr] = None
  name: Optional[str] = Field(default=None, min_length=1, max_length=100)
  role: Optional[str] = None
  is_active: Optional[bool] = None
