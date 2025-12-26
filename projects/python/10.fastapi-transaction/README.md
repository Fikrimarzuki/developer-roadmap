# FastAPI Transaction

## Setup & Installation
- Create virtual environment
  ```
  python -m venv .venv
  ```
- Aktifkan virutal env
  ```
  source .venv/bin/activate
  ```
  Atau
  ```
  source .venv/Scripts/activate
  ```
- Install dependencies
  ```
  pip install -r requirements.txt
  ```
  Install dev dependencies
  ```
  pip install -r dev-requirements.txt
  ```
- 

## Environment Config
Create `.env`
```
APP_NAME="Orders API"
DATABASE_URL="sqlite:///./app.db"
JWT_SECRET="your-super-secret-change-me"
ACCESS_TOKEN_MINUTES=15
REFRESH_TOKEN_DAYS=7
DEBUG=true
```

## Database & Migrations
- Create DB Schema
  ```
  make migrate
  ```
- Reset database
  ```
  make reset-db
  ```
  - Seed data
  ```
  make seed
  ```

## Run
- Run the API
  ```
  make run
  ```

## Authentication Flow
- Register
  ```
  POST /auth/register
  ```
- Login -  return access + refresh token
  ```
  POST /auth/login
  ```
- Refresh access token
  ```
  POST /auth/refresh
  ```
- Logout (revokes refresh token)
  ```
  POST /auth/logout
  ```
Access Token = short lived
Refresh token = stored in DB + revocable


## Testing
- Run all testing
  ```
  make test
  ```


## Developer Tooling
- Format
  ```
  make format
  ```
  Uses black + ruff-fix
- Lint
  ```
  make lint
  ```
  Configured in `pyproject.toml`
- Type check
  ```
  make typecheck
  ```

## Available make command
```
make run          # start server
make test         # run pytest
make migrate      # alembic upgrade head
make downgrade    # alembic downgrade -1
make seed         # seed DB
make reset-db     # reset DB + migrate + seed
make lint         # ruff check
make format       # black + ruff --fix
make typecheck    # mypy app
make dev-install  # pip install dev + runtime reqs (optional)
```
