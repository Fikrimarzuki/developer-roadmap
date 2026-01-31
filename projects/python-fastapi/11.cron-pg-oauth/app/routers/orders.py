from fastapi import APIRouter, BackgroundTasks, Depends
from sqlmodel import Session

from app.core.database import get_session
from app.core.deps import get_current_user
from app.core.email import send_order_email
from app.models.user import User
from app.schemas.order import OrderCreate, OrderDetailRead, OrderRead
from app.services.order_service import get_order_with_items, place_order

router = APIRouter(prefix="/orders", tags=["orders"])


@router.post("", response_model=OrderRead, status_code=201)
def create_order(
    payload: OrderCreate,
    background_tasks: BackgroundTasks,
    session: Session = Depends(get_session),
    user: User = Depends(get_current_user),
):
    assert user.id is not None

    order = place_order(session, user.id, [it.model_dump() for it in payload.items])
    session.commit()
    session.refresh(order)

    # kirim email di background
    background_tasks.add_task(
        send_order_email,
        user.email,
        f"Order #{order.id} Created",
        f"<p>Hi {user.name}, your order #{order.id} is created with status {order.status}.</p>",
    )

    assert order.id is not None
    return OrderRead(
        id=order.id,
        user_id=order.user_id,
        status=order.status,
        created_at=order.created_at.isoformat(),
    )


@router.get("/{order_id}", response_model=OrderDetailRead)
def get_order_detail(
    order_id: int,
    session: Session = Depends(get_session),
    user: User = Depends(get_current_user),
):
    return get_order_with_items(session, order_id, user)
