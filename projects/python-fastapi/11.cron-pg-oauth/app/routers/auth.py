from fastapi import APIRouter, Depends, Request
from sqlmodel import Session

from app.core.database import get_session
from app.core.oauth import google_callback, google_login
from app.schemas.auth import LoginPayload, RegisterPayload, TokenResponse
from app.schemas.user import UserRead
from app.services.auth_service import (
    login_with_google_userinfo,
    login_with_password,
    register_with_password,
)

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register")
def register_user(payload: RegisterPayload, session: Session = Depends(get_session)):
    user = register_with_password(
        session, payload.email, payload.name, payload.password
    )
    return UserRead(
        id=user.id,  # type: ignore[arg-type]
        email=user.email,
        name=user.name,
        role=user.role,
        is_active=user.is_active,
    )


@router.post("/login", response_model=TokenResponse)
def login_user(payload: LoginPayload, session: Session = Depends(get_session)):
    token = login_with_password(session, payload.email, payload.password)
    return TokenResponse(access_token=token)


@router.get("/google/login")
async def google_login_route(request: Request):
    return await google_login(request)


@router.get("/google/callback")
async def google_callback_route(
    request: Request, session: Session = Depends(get_session)
):
    userinfo = await google_callback(request)
    token = login_with_google_userinfo(session, userinfo)
    # Bisa redirect ke frontend dengan token, sementara return JSON
    return {"access_token": token, "token_type": "bearer", "provider": "google"}
