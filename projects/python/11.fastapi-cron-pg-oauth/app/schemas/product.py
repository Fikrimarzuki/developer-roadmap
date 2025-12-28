from pydantic import BaseModel
from typing import Optional


class ProductCreate(BaseModel):
    sku: str
    name: str
    price: int
    stock: int


class ProductRead(BaseModel):
    id: int
    sku: str
    name: str
    price: int
    stock: int


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[int] = None
    stock: Optional[int] = None
