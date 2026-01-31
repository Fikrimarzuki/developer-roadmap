from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_login_invalid():
  r = client.post("/auth/login", json={
    "email": "x@mail.com",
    "password": "wrong",
  })
  assert r.status_code == 401
