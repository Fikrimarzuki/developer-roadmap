from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
  return pwd_context.hash(password)

def verify_password(password: str, hashed: str) -> bool:
  return pwd_context.verify(password, hashed)

def create_access_token(subject: str) -> str:
  payload = {
    "sub": subject,
    "exp": datetime.utcnow() + timedelta(minutes=settings.jwt_expire_minutes),
  }
  return jwt.encode(payload, settings.jwt_secret, algorithm=settings.jwt_algorithm)

def decode_token(token: str) -> str | None:
  try:
    return jwt.decode(token, settings.jwt_secret, algorithms=[settings.jwt_algorithm])["sub"]
  except JWTError:
    return None

