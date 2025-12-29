from fastapi import HTTPException
from sqlmodel import Session, select

from app.core.config import settings
from app.core.security import create_token, hash_password, verify_password
from app.models.user import User


def register_with_password(
    session: Session, email: str, name: str, password: str
) -> User:
    if session.exec(select(User).where(User.email == email)).first():
        raise HTTPException(409, "Email already used")

    is_first = session.exec(select(User)).first() is None
    user = User(
        email=email,
        name=name,
        password_hash=hash_password(password),
        role="admin" if is_first else "user",
        is_active=True,
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def login_with_password(session: Session, email: str, password: str) -> str:
    user = session.exec(select(User).where(User.email == email)).first()
    if not user or not user.password_hash:
        raise HTTPException(401, "Invalid credentials")
    if not verify_password(password, user.password_hash):
        raise HTTPException(401, "Invalid credentials")

    return create_token(str(user.id), settings.access_token_minutes)


def login_with_google_userinfo(session: Session, userinfo: dict) -> str:
    email = userinfo.get("email")
    name = userinfo.get("name", "Google User")
    google_id = userinfo.get("sub")

    if not email or not google_id:
        raise HTTPException(400, "Invalid Google response")

    user = session.exec(select(User).where(User.google_id == google_id)).first()

    if not user:
        user = session.exec(select(User).where(User.email == email)).first()
        if user:
            user.google_id = google_id
        else:
            user = User(
                email=email,
                name=name,
                google_id=google_id,
                is_active=True,
                role="user",
            )
        session.add(user)
        session.commit()
        session.refresh(user)

    return create_token(str(user.id), settings.access_token_minutes)
