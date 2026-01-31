from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
import traceback
import logging

logger = logging.getLogger("app")

def http_exception_handler(request: Request, exc: HTTPException):
  return JSONResponse(
    status_code=exc.status_code,
    content={
      "message": exc.detail,
      "errors": None,
    },
  )


def validation_exception_handler(request: Request, exc: RequestValidationError):
  errors: dict[str, list[str]] = {}

  for e in exc.errors():
    loc = e.get("loc", [])
    field = str(loc[-1]) if loc else "body"
    errors.setdefault(field, []).append(e.get("msg", "Invalid value"))

  return JSONResponse(
    status_code=422,
    content={
      "message": "Validation error",
      "errors": errors,
    },
  )


def unhandled_exception_handler(request: Request, exc: Exception):
  logger.error("Unhandled error", exc_info=exc)

  return JSONResponse(
    status_code=500,
    content={
      "message": "Internal server error",
      "errors": None,
    },
  )
