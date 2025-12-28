from pydantic import BaseModel, EmailStr


class RegisterPayload(BaseModel):
    email: EmailStr
    name: str
    password: str


class LoginPayload(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
