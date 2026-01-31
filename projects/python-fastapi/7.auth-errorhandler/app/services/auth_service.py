from fastapi import HTTPException
from sqlmodel import Session, select

from app.models.user import User
from app.core.security import hash_password, verify_password, create_access_token

def register(session: Session, name: str, email: str, password: str) -> User:
  # email unique
  exists = session.exec(select(User).where(User.email == email)).first()
  if exists:
    raise HTTPException(status_code=409, detail="email already used")

  # first user becomes admin
  any_user = session.exec(select(User).limit(1)).first()
  role = "admin" if not any_user else "user"

  user = User(
    name=name,
    email=email,
    password_hash=hash_password(password),
    role=role,
    is_active=True,
  )
  session.add(user)
  session.commit()
  session.refresh(user)
  return user

def login(session: Session, email: str, password: str) -> str:
  user = session.exec(select(User).where(User.email == email)).first()
  if not user:
    raise HTTPException(status_code=401, detail="Invalid credentials")

  if not user.is_active:
    raise HTTPException(status_code=403, detail="User inactive")

  if not verify_password(password, user.password_hash):
    raise HTTPException(status_code=401, detail="Invalid credentials")

  return create_access_token(subject=str(user.id))
