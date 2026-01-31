from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
import logging
import traceback

from app.core.config import settings

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

  for err in exc.errors():
    loc = err.get("loc", [])
    field = loc[-1] if loc else "body"
    errors.setdefault(str(field), []).append(err.get("msg", "Invalid value"))

  return JSONResponse(
    status_code=422,
    content={
      "message": "Validation error",
      "errors": errors,
    },
  )


def unhandled_exception_handler(request: Request, exc: Exception):
  logger.error("Unhandled exception", exc_info=exc)

  if settings.debug:
    return JSONResponse(
      status_code=500,
      content={
        "message": str(exc),
        "errors": traceback.format_exc().splitlines(),
      },
    )

  return JSONResponse(
    status_code=500,
    content={
      "message": "Internal server error",
      "errors": None,
    },
  )
