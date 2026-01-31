from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.core.database import get_session
from app.schemas.user import UserCreate, UserRead
from app.schemas.auth import LoginRequest, TokenResponse
from app.services.auth_service import register, login

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserRead, status_code=201)
def register_user(payload: UserCreate, session: Session = Depends(get_session)):
  return register(session, payload.name, payload.email, payload.password)

@router.post("/login", response_model=TokenResponse)
def login_user(payload: LoginRequest, session: Session = Depends(get_session)):
  token = login(session, payload.email, payload.password)
  return {"access_token": token, "token_type": "bearer"}
