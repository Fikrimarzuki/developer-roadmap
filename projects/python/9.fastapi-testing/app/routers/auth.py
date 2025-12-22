from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.core.database import get_session
from app.services.auth_service import login, refresh, logout

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
def login_user(data: dict, session: Session = Depends(get_session)):
  access, refresh_token = login(
    session, data["email"], data["password"]
  )
  return {
    "access_token": access,
    "refresh_token": refresh_token,
    "token_type": "bearer",
  }

@router.post("/refresh")
def refresh_token(data: dict, session: Session = Depends(get_session)):
  return {
    "access_token": refresh(session, data["refresh_token"])
  }

@router.post("/logout")
def logout_user(data: dict, session: Session = Depends(get_session)):
  logout(session, data["refresh_token"])
  return {"ok": True}
