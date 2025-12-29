from sqlmodel import Session, select

from app.core.database import engine
from app.core.security import hash_password
from app.models.product import Product
from app.models.user import User


def seed():
    with Session(engine) as s:
        if s.exec(select(User)).first():
            print("Seed skipped: users already exist")
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
            Product(sku="SKU-001", name="Keyboard", price=250000, stock=10),
            Product(sku="SKU-002", name="Mouse", price=150000, stock=20),
            Product(sku="SKU-003", name="Monitor", price=2000000, stock=5),
        ]
        for p in products:
            s.add(p)

        s.commit()
        print("Seeded admin, user, and products")


if __name__ == "__main__":
    seed()
