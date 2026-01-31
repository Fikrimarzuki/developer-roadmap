from sqlmodel import Session, select
from app.core.database import engine
from app.models.user import User
from app.core.security import hash_password

def seed():
  with Session(engine) as s:
    exists = s.exec(select(User)).first()
    if exists:
      print("Seed skipped: users already exist")
      return

    admin = User(
      email="admin@mail.com",
      name="Admin",
      password_hash=hash_password("admin123"),
      role="admin",
      is_active=True,
    )
    s.add(admin)
    s.commit()
    print("Seeded admin user")

if __name__ == "__main__":
  seed()
