from datetime import datetime, timedelta
from fastapi import HTTPException
from sqlmodel import Session, select
from app.core.config import settings
from app.core.security import hash_password, verify_password, create_token
from app.models.user import User
from app.models.token import RefreshToken

def register(session: Session, email: str, name: str, password: str) -> User:
  if session.exec(select(User).where(User.email == email)).first():
    raise HTTPException(409, "Email already used")

  is_first = session.exec(select(User)).first() is None
  user = User(
    email=email,
    name=name,
    password_hash=hash_password(password),
    role="admin" if is_first else "user",
    is_active=True,
  )
  session.add(user)
  session.commit()
  session.refresh(user)
  return user

def login(session: Session, email: str, password: str):
  user = session.exec(select(User).where(User.email == email)).first()
  if not user or not verify_password(password, user.password_hash):
    raise HTTPException(401, "Invalid credentials")

  access = create_token(str(user.id), settings.access_token_minutes)
  refresh = create_token(str(user.id), settings.refresh_token_days * 24 * 60)

  rt = RefreshToken(
    user_id=user.id,
    token=refresh,
    expires_at=datetime.utcnow() + timedelta(days=settings.refresh_token_days),
    revoked=False,
  )
  session.add(rt)
  session.commit()

  return access, refresh

def refresh_access(session: Session, refresh_token: str) -> str:
  rt = session.exec(
    select(RefreshToken).where(
      RefreshToken.token == refresh_token,
      RefreshToken.revoked == False,
    )
  ).first()
  if not rt or rt.expires_at < datetime.utcnow():
    raise HTTPException(401, "Invalid refresh token")

  return create_token(str(rt.user_id), settings.access_token_minutes)

def logout(session: Session, refresh_token: str) -> None:
  rt = session.exec(select(RefreshToken).where(RefreshToken.token == refresh_token)).first()
  if rt:
    rt.revoked = True
    session.add(rt)
    session.commit()
