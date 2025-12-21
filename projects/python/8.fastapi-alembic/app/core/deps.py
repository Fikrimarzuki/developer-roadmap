from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlmodel import Session

from app.core.database import get_session
from app.core.security import decode_token
from app.models.user import User

bearer = HTTPBearer(auto_error=False)

def get_current_user(
  creds: HTTPAuthorizationCredentials = Depends(bearer),
  session: Session = Depends(get_session),
) -> User:
  if not creds:
    raise HTTPException(status_code=401, detail="Missing token")

  user_id = decode_token(creds.credentials)
  if not user_id:
    raise HTTPException(status_code=401, detail="Invalid token")

  user = session.get(User, int(user_id))
  if not user:
    raise HTTPException(status_code=401, detail="User not found")

  if not user.is_active:
    raise HTTPException(status_code=403, detail="User inactive")

  return user

def require_admin(user: User = Depends(get_current_user)) -> User:
  if user.role != "admin":
    raise HTTPException(status_code=403, detail="Forbidden")
  return user
