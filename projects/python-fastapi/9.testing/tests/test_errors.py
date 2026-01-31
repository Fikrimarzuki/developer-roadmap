def test_http_exception_format(client):
  # 401 from protected endpoint
  r = client.get("/users/me")

  assert r.status_code == 401
  body = r.json()

  assert body["message"] == "Missing token"
  assert body["errors"] is None


def test_validation_error_format(client):
  # login without required fields
  r = client.post("/auth/login", json={})

  assert r.status_code == 422
  body = r.json()

  assert body["message"] == "Validation error"
  assert isinstance(body["errors"], dict)
  assert "email" in body["errors"]
  assert "password" in body["errors"]


def test_unhandled_exception_format(client):
  r = client.get("/debug/boom")

  assert r.status_code == 500
  body = r.json()

  assert body["message"] in [
    "Internal server error",
    "'NoneType' object has no attribute 'name'",  # debug=true
  ]
  assert "errors" in body
