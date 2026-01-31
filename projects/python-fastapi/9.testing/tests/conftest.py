import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, Session, create_engine
from sqlalchemy.pool import StaticPool

from app.main import app
from app.core.database import get_session
from app.core.security import hash_password

from app.models.user import User

@pytest.fixture()
def client():
  engine = create_engine(
    "sqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
  )

  SQLModel.metadata.create_all(engine)

  def override_get_session():
    with Session(engine) as session:
      yield session

  app.dependency_overrides[get_session] = override_get_session

  # seed admin + normal user
  with Session(engine) as s:
    admin = User(
      email="admin@mail.com",
      name="Admin",
      password_hash=hash_password("admin123"),
      role="admin",
      is_active=True,
    )
    user = User(
      email="user@mail.com",
      name="User",
      password_hash=hash_password("user1234"),
      role="user",
      is_active=True,
    )
    s.add(admin)
    s.add(user)
    s.commit()

  with TestClient(app, raise_server_exceptions=False) as c:
    yield c


  app.dependency_overrides.clear()
