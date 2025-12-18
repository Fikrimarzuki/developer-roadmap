from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserCreate(BaseModel):
  name: str = Field(min_length=1, max_length=100)
  email: EmailStr
  password: str = Field(min_length=6, max_length=200)

class UserUpdate(BaseModel):
  name: Optional[str] = Field(default=None, min_length=1, max_length=100)
  email: Optional[EmailStr] = None
  is_active: Optional[bool] = None
  role: Optional[str] = None  # admin-only update

class UserRead(BaseModel):
  id: int
  name: str
  email: EmailStr
  role: str
  is_active: bool
