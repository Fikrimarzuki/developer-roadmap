from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError

from app.core.database import init_db
from app.core.errors import (
  http_exception_handler,
  validation_exception_handler,
  unhandled_exception_handler,
)

from app.routers.auth import router as auth_router
from app.routers.users import router as users_router

app = FastAPI()

@app.on_event("startup")
def startup():
  init_db()

app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, unhandled_exception_handler)

app.include_router(auth_router)
app.include_router(users_router)

@app.get("/debug/boom")
def boom():
  x = None
  return x.name

