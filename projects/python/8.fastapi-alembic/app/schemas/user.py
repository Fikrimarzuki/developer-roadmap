from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
  name: str
  email: EmailStr
  password: str

class UserRead(BaseModel):
  id: int
  name: str
  email: EmailStr
  role: str
  is_active: bool

class UserUpdate(BaseModel):
  name: Optional[str] = None
  email: Optional[EmailStr] = None
  role: Optional[str] = None
  is_active: Optional[bool] = None






