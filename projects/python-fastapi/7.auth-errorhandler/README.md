# FastAPI Auth Error Handler

## Features
- User registration & login
- JWT authentication (Bearer token)
- Role-based authorization (RBAC)
- Password hashing (bcrypt)
- Global error handler (consistent response)
- SQLite database (file-based)
- SQLModel ORM
- Swagger UI auto-generated
- Clean & modular structure


## ⚙️ Environment Configuration
Create `.env` file in project root:
```env
APP_NAME="User Management API"
DATABASE_URL="sqlite:///./app.db"

JWT_SECRET="change-this-to-a-long-random-string"
JWT_ALGORITHM="HS256"
JWT_EXPIRE_MINUTES=60
```


## Setup
- Buat venv
- Aktifkan venv
- Install dependencies
- Jalankan


## Database
- SQLite
- File: `app.db`


## Authentication
- Register (User utama akan menjadi admin)
  `POST` `/auth/register`
  ```json
  {
    "name": "Admin",
    "email": "admin@mail.com",
    "password": "admin123" 
  }
  ```
- Login
  `POST` `/auth/login`
  ```json
  {
    "email": "admin@mail.com",
    "password": "admin123"
  }
  ```
- Token
  Di header tambahkan
  ```
  Authorization: Bearer <JWT_TOKEN>
  ```


## Authorization
- admin
  - Manage all users
  - Change roles
  - Delete users
- user
  - Access own profile only


## Error Response
Format
```json
{
  "message": "Validation error",
  "errors": {
    "email": ["Invalid email address"]
  }
}
```


## API Endpoints
- Auth
  - POST /auth/register
  - POST /auth/login
- User
  - GET
  - POST
  - PATCH
  - DELETE
  






