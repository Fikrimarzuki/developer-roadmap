from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.core.database import get_session
from app.core.deps import require_admin
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductRead, ProductUpdate

router = APIRouter(prefix="/products", tags=["products"])

@router.post("", response_model=ProductRead, status_code=201)
def create_product(
  payload: ProductCreate,
  session: Session = Depends(get_session),
  _=Depends(require_admin),
):
  if session.exec(select(Product).where(Product.sku == payload.sku)).first():
    raise HTTPException(409, "SKU already used")
  p = Product(**payload.model_dump())
  session.add(p)
  session.commit()
  session.refresh(p)
  return p

@router.get("", response_model=list[ProductRead])
def list_products(session: Session = Depends(get_session)):
  return list(session.exec(select(Product)).all())

@router.patch("/{product_id}", response_model=ProductRead)
def update_product(
  product_id: int,
  payload: ProductUpdate,
  session: Session = Depends(get_session),
  _=Depends(require_admin),
):
  p = session.get(Product, product_id)
  if not p:
    raise HTTPException(404, "Product not found")
  data = payload.model_dump(exclude_unset=True)
  for k, v in data.items():
    setattr(p, k, v)
  session.add(p)
  session.commit()
  session.refresh(p)
  return p
