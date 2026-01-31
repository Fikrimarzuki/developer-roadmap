# tests/conftest.py
from typing import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import text
from sqlalchemy.pool import StaticPool
from sqlmodel import Session, SQLModel, create_engine, select

from app.core.database import get_session
from app.core.security import hash_password
from app.main import app
from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.product import Product
from app.models.user import User

# Pakai SQLite in-memory untuk test
TEST_DATABASE_URL = "sqlite://"

# 👉 INI yang dimaksud test_engine
test_engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)


def init_test_db() -> None:
    # pastikan semua model ter-import sebelum create_all
    _ = (User, Product, Order, OrderItem)

    # buat semua tabel (user, product, order, orderitem)
    SQLModel.metadata.create_all(test_engine)

    with Session(test_engine) as s:
        # ⚠️ PENTING: SELALU buat / recreate VIEW di SQLite test DB
        s.exec(text("DROP VIEW IF EXISTS v_order_summary"))
        s.exec(
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

        # kalau sudah ada user, anggap sudah seed (tapi VIEW sudah dibuat di atas)
        if s.exec(select(User)).first():
            return

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

        products = [
            Product(sku="SKU-001", name="Keyboard", price=300000, stock=10),
            Product(sku="SKU-002", name="Mouse", price=150000, stock=20),
            Product(sku="SKU-003", name="Monitor", price=2000000, stock=5),
        ]
        for p in products:
            s.add(p)

        s.commit()


def override_get_session() -> Generator[Session, None, None]:
    # semua request di test pakai test_engine
    with Session(test_engine) as session:
        yield session


@pytest.fixture(scope="session", autouse=True)
def setup_db() -> None:
    # dipanggil sekali per session test
    init_test_db()


@pytest.fixture()
def client() -> TestClient:
    # override dependency DB ke test_engine
    app.dependency_overrides[get_session] = override_get_session
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()
