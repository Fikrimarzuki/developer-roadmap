from fastapi import HTTPException
from sqlmodel import Session, select
from app.models.user import User
from app.core.security import hash_password, verify_password, create_access_token

def register(session: Session, name: str, email: str, password: str) -> User:
  if session.exec(select(User).where(User.email == email)).first():
    raise HTTPException(409, "Email already used")

  is_first = session.exec(select(User)).first() is None

  user = User(
    name=name,
    email=email,
    password_hash=hash_password(password),
    role="admin" if is_first else "user",
  )
  session.add(user)
  session.commit()
  session.refresh(user)
  return user

def login(session: Session, email: str, password: str) -> str:
  user = session.exec(select(User).where(User.email == email)).first()
  if not user or not verify_password(password, user.password_hash):
    raise HTTPException(401, "Invalid credentials")

  return create_access_token(str(user.id))
