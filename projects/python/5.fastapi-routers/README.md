# FastAPI CRUD with JSON and routers

## Prequesite
- siapkan venv
- aktifkan venv
- install fastapi
- tambahkan file db.json
- jalankan
  ```
  fastapi dev main.py
  ```


## Features
- Create, Read, Update, Delete user
- JSON file sebagai penyimpanan data (`db.json`)
- Swagger UI otomatis
- Modular structure (router, service, data layer)
- Tanpa ORM, tanpa database dan tanpa pydantic


## Project Structure
```
project/
├─ main.py # App bootstrap
├─ users_router.py # Router / controller
├─ users_service.py # Business logic
├─ json_db.py # JSON file data access
├─ db.json # Database file
├─ README.md
└─ .venv/
```


## Database (JSON File)
```json
[
  {
    "id": 1,
    "name": "Fikri",
    "email": "fikri@mail.com",
    "is_active": true
  }
]
```


## API Endpoints
- `Get` users
- `Post` users
  ```json
  {
    "name": "Python",
    "email": "pythonia@mail.com",
    "is_active": true
  }
  ```
- `Get` user by id
- `Update` user (replace)
- `Update` user (partial)
- `Delete` user

