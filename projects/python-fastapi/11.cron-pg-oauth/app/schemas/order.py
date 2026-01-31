from typing import List

from pydantic import BaseModel


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


class OrderItemRead(BaseModel):
    product_id: int
    product_name: str
    quantity: int
    price_each: int
    line_total: int


class OrderDetailRead(BaseModel):
    id: int
    user_id: int
    status: str
    created_at: str
    items: List[OrderItemRead]
    total_items: int
    total_amount: int
