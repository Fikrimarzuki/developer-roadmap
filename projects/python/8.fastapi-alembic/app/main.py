from fastapi import fastapi

app = FastAPI(title="FastAPI Alembic")

@app.get("/")
  return {"ok": True}


