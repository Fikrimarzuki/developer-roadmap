# FastAPI User Management API

## Features
- User registration & login
- JWT authentication (Bearer token)
- Role-based authorization (admin / user)
- Password hashing (bcrypt)
- Global error handler (consistent error response)
- SQLite database (file-based)
- SQLModel ORM
- Alembic migration
- Database seeder
- Swagger UI (OpenAPI)


## Environment Configuration
Create `.env` file in project root:
```env
APP_NAME="User Management API"
DATABASE_URL="sqlite:///./app.db"

JWT_SECRET="change-this-to-a-long-random-string"
JWT_ALGORITHM="HS256"
JWT_EXPIRE_MINUTES=60

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


## Database
- Type: SQLite
- File: app.db
- Auto created
- Skema dimanage lewat `Alembic migration`
- Apply migration
  ```
  alembic upgrade head
  ```
- Seed initial admin
  ```
  python -m app.seed
  ```
  Default user
  admin 
  ```
  email: admin@mail.com
  password: admin123
  role: admin
  ```


## Authentication Flow
- Register (User pertama akan menjadi admin)<br/>
  POST /auth/register
  ```
  {
    "name": "Admin",
    "email": "admin@mail.com",
    "password": "admin123"
  }
  ```
- Login<br/>
  POST /auth/login
  ```
  {
    "email": "admin@mail.com",
    "password": "admin123"
  }
  ```
- Token
  ```
  Authorization: Bearer <JWT_TOKEN>
  ```


## Error Handler
- Validation Error
  ```
  {
    "message": "Validation error",
    "errors": {
      "email": ["Invalid email address"]
    }
  }
  ```
- Business Error (`HTTPException`)
  ```
  {
    "message": "Email already used",
    "errors": null
  }
  ```
- Unhandled Error (500)
  ```
  {
    "message": "Internal server error",
    "errors": null
  }
  ```
  




