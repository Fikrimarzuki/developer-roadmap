def login(client, email: str, password: str) -> str:
  r = client.post("/auth/login", json={"email": email, "password": password})
  assert r.status_code == 200, r.text
  return r.json()["access_token"]

def auth_headers(token: str) -> dict:
  return {"Authorization": f"Bearer {token}"}
