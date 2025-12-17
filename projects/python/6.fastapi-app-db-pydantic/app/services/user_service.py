from typing import List
from fastapi import HTTPException
from sqlmodel import Session, select

from app.models.user import User
from app.schemas.user import UserCreate, UserReplace, UserUpdate


def create_user(session: Session, payload: UserCreate) -> User:
  # email unique check
  exists = session.exec(select(User).where(User.email == payload.email)).first()
  if exists:
    raise HTTPException(status_code=409, detail="email already used")

  user = User(name=payload.name, email=payload.email, is_active=payload.is_active)
  session.add(user)
  session.commit()
  session.refresh(user)
  return user


def list_users(session: Session) -> List[User]:
  return list(session.exec(select(User)).all())


def get_user(session: Session, user_id: int) -> User:
  user = session.get(User, user_id)
  if not user:
    raise HTTPException(status_code=404, detail="User not found")
  return user


def replace_user(session: Session, user_id: int, payload: UserReplace) -> User:
  user = get_user(session, user_id)

  exists = session.exec(
    select(User).where(User.email == payload.email, User.id != user_id)
  ).first()
  if exists:
    raise HTTPException(status_code=409, detail="email already used")

  user.name = payload.name
  user.email = payload.email
  user.is_active = payload.is_active

  session.add(user)
  session.commit()
  session.refresh(user)
  return user


def update_user(session: Session, user_id: int, payload: UserUpdate) -> User:
  user = get_user(session, user_id)

  if payload.email is not None:
    exists = session.exec(
      select(User).where(User.email == payload.email, User.id != user_id)
    ).first()
    if exists:
      raise HTTPException(status_code=409, detail="email already used")
    user.email = payload.email

  if payload.name is not None:
    user.name = payload.name

  if payload.is_active is not None:
    user.is_active = payload.is_active

  session.add(user)
  session.commit()
  session.refresh(user)
  return user


def delete_user(session: Session, user_id: int) -> None:
  user = get_user(session, user_id)
  session.delete(user)
  session.commit()
