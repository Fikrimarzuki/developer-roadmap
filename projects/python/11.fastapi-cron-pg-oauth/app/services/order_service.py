from fastapi import HTTPException
from sqlmodel import Session, select

from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.product import Product
from app.models.user import User
from app.schemas.order import OrderDetailRead, OrderItemRead


def place_order(session: Session, user_id: int, items: list[dict]) -> Order:
    if not items:
        raise HTTPException(422, "items is required")

    order = Order(user_id=user_id, status="pending")
    session.add(order)
    session.flush()  # supaya order.id terisi

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


def get_order_with_items(
    session: Session,
    order_id: int,
    current: User,
) -> OrderDetailRead:
    order = session.get(Order, order_id)
    if not order:
        raise HTTPException(404, "Order not found")

    if current.role != "admin" and order.user_id != current.id:
        raise HTTPException(403, "Forbidden")

    stmt = (
        select(OrderItem, Product)
        .join(Product, Product.id == OrderItem.product_id)  # type: ignore[arg-type]
        .where(OrderItem.order_id == order.id)
    )
    rows = session.exec(stmt).all()

    items: list[OrderItemRead] = []
    total_items = 0
    total_amount = 0

    for oi, p in rows:
        assert p.id is not None
        line_total = oi.quantity * oi.price_each
        items.append(
            OrderItemRead(
                product_id=p.id,
                product_name=p.name,
                quantity=oi.quantity,
                price_each=oi.price_each,
                line_total=line_total,
            )
        )
        total_items += oi.quantity
        total_amount += line_total

    assert order.id is not None

    return OrderDetailRead(
        id=order.id,
        user_id=order.user_id,
        status=order.status,
        created_at=order.created_at.isoformat(),
        items=items,
        total_items=total_items,
        total_amount=total_amount,
    )
