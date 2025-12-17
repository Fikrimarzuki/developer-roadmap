from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
  name: str = Field(min_length=1, max_length=100)
  email: EmailStr
  is_active: bool = True

class UserReplace(BaseModel):
  name: str = Field(min_length=1, max_length=100)
  email: EmailStr
  is_active: bool = True

class UserUpdate(BaseModel):
  name: Optional[str] = Field(default=None, min_length=1, max_length=100)
  email: Optional[EmailStr] = None
  is_active: Optional[bool] = None

class UserRead(BaseModel):
  id: int
  name: str
  email: EmailStr
  is_active: bool


