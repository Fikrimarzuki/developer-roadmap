from fastapi import HTTPException
from sqlmodel import Session, select

from app.models.user import User
from app.schemas.user import UserUpdate


def list_users(session: Session) -> list[User]:
  return list(session.exec(select(User)).all())


def get_user(session: Session, user_id: int) -> User:
  user = session.get(User, user_id)
  if not user:
    raise HTTPException(404, "User not found")
  return user


def update_user_admin(
  session: Session,
  user_id: int,
  payload: UserUpdate,
) -> User:
  user = get_user(session, user_id)

  if payload.email is not None:
    exists = session.exec(
      select(User).where(User.email == payload.email, User.id != user_id)
    ).first()
    if exists:
      raise HTTPException(409, "Email already used")
    user.email = payload.email

  if payload.name is not None:
    user.name = payload.name

  if payload.role is not None:
    if payload.role not in ["admin", "user"]:
      raise HTTPException(422, "Invalid role")
    user.role = payload.role

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
