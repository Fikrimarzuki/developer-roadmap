from fastapi import HTTPException
from sqlmodel import Session
from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.product import Product

def place_order(session: Session, user_id: int, items: list[dict]) -> Order:
  if not items:
    raise HTTPException(422, "items is required")

  # with session.begin():
  order = Order(user_id=user_id, status="pending")
  session.add(order)
  session.flush()  # ensures order.id available

  for it in items:
    pid = int(it["product_id"])
    qty = int(it["quantity"])
    
    if qty <= 0:
      raise HTTPException(422, "quantity must be > 0")

    product = session.get(Product, pid)
    if not product:
      raise HTTPException(404, f"Product {pid} not found")

    if product.stock < qty:
      raise HTTPException(409, f"Insufficient stock for product {pid}")

    product.stock -= qty
    session.add(product)

    oi = OrderItem(
      order_id=order.id,
      product_id=pid,
      quantity=qty,
      price_each=product.price,
    )
    session.add(oi)

  return order
