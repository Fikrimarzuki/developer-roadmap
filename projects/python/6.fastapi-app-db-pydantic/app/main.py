from fastapi import FastAPI

from app.core.config import settings
from app.core.database import init_db
from app.routers.users import router as users_router

app = FastAPI(title=settings.app_name)

@app.on_event("startup")
def on_startup() -> None:
  init_db()

@app.get("/")
def root():
  return {"ok": True, "docs": "/docs"}

app.include_router(users_router)
