from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.core.database import get_session
from app.schemas.auth import LoginRequest, LogoutRequest, RefreshRequest, TokenResponse
from app.schemas.user import UserCreate, UserRead
from app.services.auth_service import login, logout, refresh_access, register

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserRead)
def register_user(payload: UserCreate, session: Session = Depends(get_session)):
    return register(session, payload.email, payload.name, payload.password)


@router.post("/login", response_model=TokenResponse)
def login_user(payload: LoginRequest, session: Session = Depends(get_session)):
    access, refresh = login(session, payload.email, payload.password)
    return TokenResponse(access_token=access, refresh_token=refresh)


@router.post("/refresh")
def refresh_token(payload: RefreshRequest, session: Session = Depends(get_session)):
    access = refresh_access(session, payload.refresh_token)
    return {"access_token": access, "token_type": "bearer"}


@router.post("/logout")
def logout_user(payload: LogoutRequest, session: Session = Depends(get_session)):
    logout(session, payload.refresh_token)
    return {"ok": True}
