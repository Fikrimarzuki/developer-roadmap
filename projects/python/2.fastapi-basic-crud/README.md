# FastAPI CRUD with venv

## Bikin Virtual env
```bash
python -m venv .venv
```
Atau
```bash
python3 -m venv .venv
```

## Aktifkan venv
- Windows
  ```
  .venv\Scripts\activate
  ```
- MacOS/Linux
  ```
  source .venv/bin/activate
  ```
- Bash dan di windows
  ```
  source .venv/Scripts/activate
  ```
- Kalau berhasil akan ada tulisan
  ```
  (.venv)
  ```

## Install FastAPI + Server
```
pip install "fastapi[standard]"
```

## Run with FastAPI
```
fastapi dev main.py
```

## Buka
- http://127.0.0.1:8000 akan akses home yang memperlihakan JSON
- http://127.0.0.1:8000/docs akan membuka swagger UI otomatis

## Run with uvicorn
```
uvicorn main:app --reload
```

## Untuk menonaktifkan venv
```
deactivate
```

