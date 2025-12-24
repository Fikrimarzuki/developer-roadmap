from fastapi import APIRouter, Depends
from app.core.deps import get_current_user, require_admin
from app.models.user import User
from app.schemas.user import UserRead

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me", response_model=UserRead)
def me(current: User = Depends(get_current_user)):
  return current

@router.get("/admin-only")
def admin_only(_: User = Depends(require_admin)):
  return {"ok": True}
