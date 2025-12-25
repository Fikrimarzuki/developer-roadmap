import pytest
from fastapi.testclient import TestClient
from sqlalchemy import event, text
from sqlalchemy.pool import StaticPool
from sqlmodel import Session, SQLModel, create_engine

from app.core.database import get_session
from app.core.security import hash_password
from app.main import app
from app.models.product import Product
from app.models.user import User


@pytest.fixture()
def client():
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )

    @event.listens_for(engine, "connect")
    def _fk_on(dbapi_connection, _):
        cur = dbapi_connection.cursor()
        cur.execute("PRAGMA foreign_keys=ON;")
        cur.close()

    SQLModel.metadata.create_all(engine)

    # create view for tests (since create_all doesn't create views)
    with engine.connect() as conn:
        conn.execute(
            text(
                """
    CREATE VIEW v_order_summary AS
    SELECT
      o.id AS order_id,
      o.user_id AS user_id,
      COUNT(oi.id) AS total_items,
      COALESCE(SUM(oi.quantity * oi.price_each), 0) AS total_amount
    FROM "order" o
    LEFT JOIN orderitem oi ON oi.order_id = o.id
    GROUP BY o.id, o.user_id
    """
            )
        )
        conn.commit()

    def override_get_session():
        with Session(engine) as session:
            yield session

    app.dependency_overrides[get_session] = override_get_session

    # seed admin + user + products
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
        s.add(Product(sku="SKU-001", name="Keyboard", price=250000, stock=2))
        s.add(Product(sku="SKU-002", name="Mouse", price=150000, stock=10))
        s.commit()

    with TestClient(app, raise_server_exceptions=False) as c:
        yield c

    app.dependency_overrides.clear()
