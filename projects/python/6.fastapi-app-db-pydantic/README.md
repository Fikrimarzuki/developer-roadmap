# FastAPI (app db pydantic)

## ✨ Features
- Create, Read, Update, Delete User
- SQLite database (file-based)
- SQLModel (ORM)
- Pydantic schemas (request & response)
- Environment config (`.env`)
- Swagger UI otomatis
- Modular & scalable structure
- Requirements.txt

## Environment Configuration
Create `.env` file ini di project roo
```env
APP_NAME="User CRUD API"
DATABASE_URL="sqlite:///./app.db"
```

## Setup
- Buat venv
  ```
  python -m venv .venv
  ```
- Aktifkan venv
  - Bash Windows
  ```
  source .venv/Scripts/activate
  ```
- Cek
  ```
  which python
  ```
  Harus mengarah ke
  ```
  .../.venv/Scripts/python
  ```
- Install Dependencies
  ```
  pip install "fastapi[standard]" sqlmodel pydantic-settings
  ```
  Atau
  ```
  pip install -r requirements.txt
  ```
- Jalankan
  ```
  fastapi dev app/main.py
  ```

## Database
- Database type: SQLite
- Database file: app.db
- Terbuat otomatis pada saat app berjalan pertama kali
- Tabel terbuat otomatis lewat SQLModel 
- View Database
  - DBeaver
    - New connection -> SQLite
    - Select database file
      ```
      path/to/project/app.db
      ```
  - SQLite CLI
    - Jalankan
      ```
      sqlite3 app
      ```
    - Di prompt
      ```sql
      .tables
      SELECT * FROM user;
      ```
    - Untuk keluar
      ```
      .quit
      ```


## Note
- File __init__.py boleh kosong, tapi wajib ada agar Python anggap folder sebagai package.
- Database menggunakan sqlite

## Endpoint
- Get Root - GET /
- Create User - POST /users
- Get All User - GET /users
- Get User by ID - GET /users/{user_id}
- Update User (Replace) - PUT /users/{user_id}
- Update User (Partial) - PATCH /users/{user_id}
- Delete User - DELETE /users/{user_id}
