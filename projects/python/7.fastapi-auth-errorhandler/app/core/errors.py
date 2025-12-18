from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

def http_exception_handler(request: Request, exc: HTTPException):
  return JSONResponse(
    status_code=exc.status_code,
    content={"message": exc.detail, "errors": None},
  )

def validation_exception_handler(request: Request, exc: RequestValidationError):
  errors: dict[str, list[str]] = {}
  for e in exc.errors():
    loc = e.get("loc", [])
    field = str(loc[-1]) if loc else "body"
    errors.setdefault(field, []).append(e.get("msg", "Invalid value"))

  return JSONResponse(
    status_code=422,
    content={"message": "Validation error", "errors": errors},
  )
