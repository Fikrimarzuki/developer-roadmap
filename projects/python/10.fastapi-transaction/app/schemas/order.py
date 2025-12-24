from pydantic import BaseModel
from typing import List

class OrderItemCreate(BaseModel):
  product_id: int
  quantity: int

class OrderCreate(BaseModel):
  items: List[OrderItemCreate]

class OrderRead(BaseModel):
  id: int
  user_id: int
  status: str
  created_at: str
