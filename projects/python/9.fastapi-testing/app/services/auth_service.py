from datetime import datetime, timedelta
from fastapi import HTTPException
from sqlmodel import Session, select

from app.models.user import User
from app.models.token import RefreshToken
from app.core.security import (
  hash_password,
  verify_password,
  create_token,
)
from app.core.config import settings

def login(session: Session, email: str, password: str):
  user = session.exec(select(User).where(User.email == email)).first()
  if not user or not verify_password(password, user.password_hash):
    raise HTTPException(401, "Invalid credentials")

  access = create_token(str(user.id), settings.access_token_minutes)
  refresh = create_token(
    str(user.id),
    settings.refresh_token_days * 24 * 60,
  )

  session.add(
    RefreshToken(
      user_id=user.id,
      token=refresh,
      expires_at=datetime.utcnow()
      + timedelta(days=settings.refresh_token_days),
    )
  )
  session.commit()

  return access, refresh

def refresh(session: Session, refresh_token: str):
  token = session.exec(
    select(RefreshToken).where(
      RefreshToken.token == refresh_token,
      RefreshToken.revoked == False,
    )
  ).first()

  if not token or token.expires_at < datetime.utcnow():
    raise HTTPException(401, "Invalid refresh token")

  access = create_token(
    str(token.user_id), settings.access_token_minutes
  )
  return access

def logout(session: Session, refresh_token: str):
  token = session.exec(
    select(RefreshToken).where(RefreshToken.token == refresh_token)
  ).first()

  if token:
    token.revoked = True
    session.add(token)
    session.commit()
