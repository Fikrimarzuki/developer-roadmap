from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
  email: EmailStr
  name: str
  password: str

class UserRead(BaseModel):
  id: int
  email: EmailStr
  name: str
  role: str
  is_active: bool

class UserUpdate(BaseModel):
  email: Optional[EmailStr] = None
  name: Optional[str] = None
  role: Optional[str] = None
  is_active: Optional[bool] = None
