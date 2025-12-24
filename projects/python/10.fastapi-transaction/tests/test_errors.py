def test_http_exception_format(client):
  r = client.get("/users/me")
  assert r.status_code == 401
  body = r.json()
  assert body["message"] == "Missing token"
  assert body["errors"] is None

def test_validation_error_format(client):
  r = client.post("/auth/login", json={})
  assert r.status_code == 422
  body = r.json()
  assert body["message"] == "Validation error"
  assert "email" in body["errors"]
  assert "password" in body["errors"]
