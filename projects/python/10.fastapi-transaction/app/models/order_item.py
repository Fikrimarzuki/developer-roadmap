from typing import Optional
from sqlmodel import SQLModel, Field

class OrderItem(SQLModel, table=True):
  id: Optional[int] = Field(default=None, primary_key=True)
  order_id: int = Field(index=True, foreign_key="order.id")
  product_id: int = Field(index=True, foreign_key="product.id")
  quantity: int
  price_each: int
