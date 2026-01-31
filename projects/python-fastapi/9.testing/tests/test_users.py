def login(client, email: str, password: str) -> str:
  r = client.post("/auth/login", json={"email": email, "password": password})
  assert r.status_code == 200, r.text
  return r.json()["access_token"]

def auth_headers(token: str) -> dict:
  return {"Authorization": f"Bearer {token}"}

def test_users_me_requires_auth(client):
  r = client.get("/users/me")
  assert r.status_code == 401

def test_users_me_ok(client):
  token = login(client, "user@mail.com", "user1234")
  r = client.get("/users/me", headers=auth_headers(token))
  assert r.status_code == 200
  data = r.json()
  assert data["email"] == "user@mail.com"
  assert data["role"] == "user"

def test_admin_list_users_ok(client):
  token = login(client, "admin@mail.com", "admin123")
  r = client.get("/users", headers=auth_headers(token))
  assert r.status_code == 200
  assert isinstance(r.json(), list)
  assert len(r.json()) >= 2

def test_non_admin_list_users_forbidden(client):
  token = login(client, "user@mail.com", "user1234")
  r = client.get("/users", headers=auth_headers(token))
  assert r.status_code == 403
  body = r.json()
  assert body["message"] == "Forbidden"
  assert body["errors"] is None

def test_admin_patch_user_role(client):
  admin_token = login(client, "admin@mail.com", "admin123")

  # get user list, find the normal user id
  users = client.get("/users", headers=auth_headers(admin_token)).json()
  normal_user = next(u for u in users if u["email"] == "user@mail.com")
  user_id = normal_user["id"]

  r = client.patch(
    f"/users/{user_id}",
    headers=auth_headers(admin_token),
    json={"role": "admin"},
  )
  assert r.status_code == 200, r.text
  assert r.json()["role"] == "admin"

def test_admin_delete_user(client):
  admin_token = login(client, "admin@mail.com", "admin123")

  users = client.get("/users", headers=auth_headers(admin_token)).json()
  target = next(u for u in users if u["email"] == "user@mail.com")
  user_id = target["id"]

  r = client.delete(f"/users/{user_id}", headers=auth_headers(admin_token))
  assert r.status_code == 204

  # confirm deleted
  r2 = client.get(f"/users/{user_id}", headers=auth_headers(admin_token))
  assert r2.status_code == 404
