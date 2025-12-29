from fastapi import status


def login(client, email: str, password: str) -> str:
    r = client.post("/auth/login", json={"email": email, "password": password})
    assert r.status_code == 200, r.text
    return r.json()["access_token"]


def auth_headers(token: str) -> dict:
    return {"Authorization": f"Bearer {token}"}


def ensure_one_order(client, token: str):
    # bikin 1 order supaya summary tidak kosong
    r_products = client.get("/products", headers=auth_headers(token))
    assert r_products.status_code == status.HTTP_200_OK
    p = r_products.json()[0]

    r = client.post(
        "/orders",
        headers=auth_headers(token),
        json={"items": [{"product_id": p["id"], "quantity": 1}]},
    )
    assert r.status_code == status.HTTP_201_CREATED


def test_user_order_summary(client):
    token = login(client, "user@mail.com", "user1234")
    ensure_one_order(client, token)

    r = client.get("/reports/orders/summary", headers=auth_headers(token))
    assert r.status_code == status.HTTP_200_OK, r.text
    rows = r.json()
    assert isinstance(rows, list)
    assert len(rows) >= 1

    # struktur minimal: order_id, user_id, total_items, total_amount
    row = rows[0]
    assert "order_id" in row
    assert "user_id" in row
    assert "total_items" in row
    assert "total_amount" in row


def test_admin_all_order_summary(client):
    user_token = login(client, "user@mail.com", "user1234")
    ensure_one_order(client, user_token)

    admin_token = login(client, "admin@mail.com", "admin123")
    r = client.get(
        "/reports/orders/summary/all",
        headers=auth_headers(admin_token),
    )
    assert r.status_code == status.HTTP_200_OK, r.text
    rows = r.json()
    assert isinstance(rows, list)
    assert len(rows) >= 1
