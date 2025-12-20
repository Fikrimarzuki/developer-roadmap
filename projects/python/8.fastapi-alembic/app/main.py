from fastapi import FastAPI
from app.core.config import settings
from app.core.database import init_db
from app.routers.auth import router as auth_router

app = FastAPI(title="FastAPI Alembic")

@app.on_event("startup")
def startup():
  init_db()

app.include_router(auth_router)

@app.get("/")
def root():
  return {"ok": True}


