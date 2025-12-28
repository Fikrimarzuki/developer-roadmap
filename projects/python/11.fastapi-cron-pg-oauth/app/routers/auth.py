from fastapi import APIRouter, Depends, Request
from sqlmodel import Session
from app.core.database import get_session
from app.core.oauth import google_login, google_callback
from app.schemas.auth import RegisterPayload, LoginPayload
from app.services.auth_service import (
    register_with_password,
    login_with_password,
    login_with_google_userinfo,
)

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register")
def register_user(payload: RegisterPayload, session: Session = Depends(get_session)):
    user = register_with_password(
        session, payload.email, payload.name, payload.password
    )
    return {"id": user.id, "email": user.email, "name": user.name}


@router.post("/login")
def login_user(payload: LoginPayload, session: Session = Depends(get_session)):
    token = login_with_password(session, payload.email, payload.password)
    return {"access_token": token, "token_type": "bearer"}


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
