# FastAPI Transaction

## Daily workflow
- setup
  ```
  python -m venv .venv
  source .venv/Scripts/activate
  pip install -r requirements.txt
  ```
- migration
  ```
  alembic upgrade head
  ```
- seed
  ```
  python -m app.seed
  ```
- run
  ```
  fastapi dev app/main.py
  ```
- test
  ```
  pytest -q
  ```
  