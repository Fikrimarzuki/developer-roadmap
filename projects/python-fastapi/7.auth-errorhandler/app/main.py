from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError

from app.core.config import settings
from app.core.database import init_db
from app.core.errors import http_exception_handler, validation_exception_handler
from app.routers.users import router as users_router
from app.routers.auth import router as auth_router

app = FastAPI(title=settings.app_name)

# Global error handlers (consistent response shape)
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)

@app.on_event("startup")
def on_startup() -> None:
  init_db()

@app.get("/")
def root():
  return {"ok": True, "docs": "/docs"}

app.include_router(auth_router)
app.include_router(users_router)
