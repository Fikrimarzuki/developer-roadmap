from sqlmodel import Session, select
from app.core.database import engine
from app.models.user import User
from app.core.security import hash_password

with Session(engine) as session:
  if session.exec(select(User)).first():
    print("Already seeded")
  else:
    admin = User(
      name="Admin",
      email="admin@mail.com",
      password_hash=hash_password("admin123"),
      role="admin",
    )
    session.add(admin)
    session.commit()
    print("Seeded admin user")


