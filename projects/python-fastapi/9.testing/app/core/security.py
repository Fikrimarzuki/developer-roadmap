from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
from app.core.config import settings

pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(p: str) -> str:
  return pwd.hash(p)

def verify_password(p: str, h: str) -> bool:
  return pwd.verify(p, h)

def create_token(subject: str, minutes: int) -> str:
  payload = {
    "sub": subject,
    "exp": datetime.utcnow() + timedelta(minutes=minutes),
  }
  return jwt.encode(payload, settings.jwt_secret, algorithm=settings.jwt_algorithm)

def decode_token(token: str) -> str | None:
  try:
    return jwt.decode(
      token, settings.jwt_secret, algorithms=[settings.jwt_algorithm]
    )["sub"]
  except JWTError:
    return None
