from fastapi import status


def login(client, email: str, password: str) -> str:
    r = client.post("/auth/login", json={"email": email, "password": password})
    assert r.status_code == 200, r.text
    return r.json()["access_token"]


def test_login_admin_ok(client):
    r = client.post(
        "/auth/login",
        json={"email": "admin@mail.com", "password": "admin123"},
    )
    assert r.status_code == status.HTTP_200_OK
    body = r.json()
    assert "access_token" in body
    assert body["token_type"] == "bearer"


def test_login_invalid_credentials(client):
    r = client.post(
        "/auth/login",
        json={"email": "admin@mail.com", "password": "salahpassword"},
    )
    assert r.status_code == status.HTTP_401_UNAUTHORIZED
