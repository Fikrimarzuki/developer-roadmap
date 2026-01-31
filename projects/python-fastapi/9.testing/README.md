# FastAPI Testing

## Features
- User login (JWT access + refresh token)
- Token refresh
- Logout (refresh token revocation)
- Protected endpoints with Bearer auth
- Admin-only user management
- Global error handler (HTTP, validation, unhandled)
- Consistent error response contract
- SQLModel ORM
- Alembic migration (upgrade & downgrade)
- In-memory database testing
- Swagger (OpenAPI) documentation


##  Environment Variables
Create `.env` in project root:
```env
APP_NAME="FastAPI Auth API"
DATABASE_URL="sqlite:///./app.db"

JWT_SECRET="super-secret-key"
JWT_ALGORITHM="HS256"

ACCESS_TOKEN_MINUTES=15
REFRESH_TOKEN_DAYS=7

DEBUG=true
```

## Setup
- Buat venv
  ```
  python -m venv .venv
  ```
- Aktivasi venv
  ```
  source .venv/Scripts/activate
  ```
  Atau
  ```
  source .venv/bin/activate
  ```
- Install dependencies
  ```
  pip install -r requirements.txt
  ```
  Notes: `bcrypt` menggunakan versi dibawah 4 agar tidak error `__about__`
- Run application
  ```
  fastapi dev app/main.py
  ```

## Testing
- Run testing
  ```
  pytest
  ```
  Apabila di windows tidak bisa coba jalankan
  ```
  python -m pytest
  ```

## Database
- Create migration
  ```
  alembic revision --autogenerate -m "message"
  ``
- Apply migration
  ```
  alembic upgrade head
  ``
- Rollback (downgrade)
  ```
  alembic downgrade -1
  ```
- Reset DB
  ```
  alembic downgrade base
  alembic upgrade head
  ``

