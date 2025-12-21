from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.core.database import get_session
from app.core.deps import get_current_user, require_admin
from app.schemas.user import UserRead, UserUpdate
from app.services.user_service import (
  list_users,
  get_user,
  update_user_admin,
  delete_user,
)
from app.models.user import User

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me", response_model=UserRead)
def me(current_user: User = Depends(get_current_user)):
  return current_user


@router.get("", response_model=list[UserRead])
def list_all(
  session: Session = Depends(get_session),
  admin: User = Depends(require_admin),
):
  return list_users(session)


@router.get("/{user_id}", response_model=UserRead)
def get_one(
  user_id: int,
  session: Session = Depends(get_session),
  admin: User = Depends(require_admin),
):
  return get_user(session, user_id)


@router.patch("/{user_id}", response_model=UserRead)
def update(
  user_id: int,
  payload: UserUpdate,
  session: Session = Depends(get_session),
  admin: User = Depends(require_admin),
):
  return update_user_admin(session, user_id, payload)


@router.delete("/{user_id}", status_code=204)
def remove(
  user_id: int,
  session: Session = Depends(get_session),
  admin: User = Depends(require_admin),
):
  delete_user(session, user_id)
  return None
