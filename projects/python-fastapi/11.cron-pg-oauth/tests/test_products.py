# tests/test_products.py
from fastapi import status


def login(client, email: str, password: str) -> str:
    r = client.post("/auth/login", json={"email": email, "password": password})
    assert r.status_code == 200, r.text
    return r.json()["access_token"]


def auth_headers(token: str) -> dict:
    return {"Authorization": f"Bearer {token}"}


def test_admin_can_create_product(client):
    token = login(client, "admin@mail.com", "admin123")

    r = client.post(
        "/products",
        headers=auth_headers(token),
        json={
            "sku": "SKU-999",
            "name": "Webcam",
            "price": 500000,
            "stock": 3,
        },
    )

    assert r.status_code == status.HTTP_201_CREATED, r.text
    body = r.json()
    assert body["sku"] == "SKU-999"
    assert body["name"] == "Webcam"
    assert body["stock"] == 3


def test_non_admin_cannot_create_product(client):
    token = login(client, "user@mail.com", "user1234")

    r = client.post(
        "/products",
        headers=auth_headers(token),
        json={
            "sku": "SKU-888",
            "name": "Speakers",
            "price": 750000,
            "stock": 2,
        },
    )

    # require_admin = 403
    assert r.status_code == status.HTTP_403_FORBIDDEN
