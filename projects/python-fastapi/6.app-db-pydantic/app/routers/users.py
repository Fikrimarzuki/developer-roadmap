from typing import List
from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.core.database import get_session
from app.schemas.user import UserCreate, UserRead, UserReplace, UserUpdate
from app.services.user_service import (
  create_user,
  delete_user,
  get_user,
  list_users,
  replace_user,
  update_user,
)

router = APIRouter(prefix="/users", tags=["users"])

@router.post("", response_model=UserRead, status_code=201)
def create(payload: UserCreate, session: Session = Depends(get_session)):
  return create_user(session, payload)

@router.get("", response_model=List[UserRead])
def list_all(session: Session = Depends(get_session)):
  return list_users(session)

@router.get("/{user_id}", response_model=UserRead)
def get_one(user_id: int, session: Session = Depends(get_session)):
  return get_user(session, user_id)

@router.put("/{user_id}", response_model=UserRead)
def put(user_id: int, payload: UserReplace, session: Session = Depends(get_session)):
  return replace_user(session, user_id, payload)

@router.patch("/{user_id}", response_model=UserRead)
def patch(user_id: int, payload: UserUpdate, session: Session = Depends(get_session)):
    return update_user(session, user_id, payload)

@router.delete("/{user_id}", status_code=204)
def remove(user_id: int, session: Session = Depends(get_session)):
  delete_user(session, user_id)
  return None



