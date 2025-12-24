from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.core.database import get_session
from app.core.deps import get_current_user
from app.models.user import User
from app.services.report_service import list_order_summaries

router = APIRouter(prefix="/reports", tags=["reports"])

@router.get("/orders/summary")
def my_order_summary(
  session: Session = Depends(get_session),
  user: User = Depends(get_current_user),
):
  return list_order_summaries(session, user_id=user.id)

@router.get("/orders/summary/all")
def all_order_summary(
  session: Session = Depends(get_session),
):
  # public for demo; you can make admin-only later
  return list_order_summaries(session, user_id=None)
