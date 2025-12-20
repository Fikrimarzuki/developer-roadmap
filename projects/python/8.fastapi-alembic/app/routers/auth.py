from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.core.database import get_session
from app.schemas.user import UserCreate, UserRead
from app.services.auth_service import register, login

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserRead)
def register_user(payload: UserCreate, session: Session = Depends(get_session)):
  return register(session, payload.name, payload.email, payload.password)

@router.post("/login")
def login_user(payload: UserCreate, session: Session = Depends(get_session)):
  token = login(session, payload.email, payload.password)
  return {"access_token": token, "token_type": "bearer"}
