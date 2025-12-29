from fastapi import status


def login(client, email: str, password: str) -> str:
    r = client.post("/auth/login", json={"email": email, "password": password})
    assert r.status_code == 200, r.text
    return r.json()["access_token"]


def auth_headers(token: str) -> dict:
    return {"Authorization": f"Bearer {token}"}


def get_products(client, token: str):
    r = client.get("/products", headers=auth_headers(token))
    assert r.status_code == status.HTTP_200_OK, r.text
    return r.json()


def test_place_order_success_and_stock_deduct(client):
    token = login(client, "user@mail.com", "user1234")

    # cek stock awal
    products_before = get_products(client, token)
    p = next(p for p in products_before if p["sku"] == "SKU-001")
    product_id = p["id"]
    stock_before = p["stock"]

    r = client.post(
        "/orders",
        headers=auth_headers(token),
        json={
            "items": [
                {"product_id": product_id, "quantity": 2},
            ]
        },
    )
    assert r.status_code == status.HTTP_201_CREATED, r.text
    body = r.json()
    assert body["status"] == "pending"
    assert body["user_id"] is not None

    # stock harus berkurang 2
    products_after = get_products(client, token)
    p_after = next(p for p in products_after if p["id"] == product_id)
    assert p_after["stock"] == stock_before - 2


def test_place_order_insufficient_stock_rollback(client):
    token = login(client, "user@mail.com", "user1234")

    # cek stock awal
    products_before = get_products(client, token)
    p = next(p for p in products_before if p["sku"] == "SKU-002")
    product_id = p["id"]
    stock_before = p["stock"]

    # pesan jumlah yang terlalu banyak
    r = client.post(
        "/orders",
        headers=auth_headers(token),
        json={
            "items": [
                {"product_id": product_id, "quantity": stock_before + 100},
            ]
        },
    )

    assert r.status_code == status.HTTP_409_CONFLICT, r.text

    # stock tetap sama (rollback)
    products_after = get_products(client, token)
    p_after = next(p for p in products_after if p["id"] == product_id)
    assert p_after["stock"] == stock_before
