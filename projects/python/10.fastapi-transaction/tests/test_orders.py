from tests.helpers import auth_headers, login


def test_place_order_success(client):
    token = login(client, "user@mail.com", "user1234")

    r = client.post(
        "/orders",
        headers=auth_headers(token),
        json={"items": [{"product_id": 1, "quantity": 1}]},
    )
    assert r.status_code == 201, r.text

    # view summary should reflect it
    s = client.get("/reports/orders/summary", headers=auth_headers(token))
    assert s.status_code == 200
    rows = s.json()
    assert len(rows) == 1
    assert rows[0]["total_amount"] == 250000


def test_place_order_rollback_on_insufficient_stock(client):
    token = login(client, "user@mail.com", "user1234")

    # product_id=1 stock=2, attempt quantity=99 should fail
    r = client.post(
        "/orders",
        headers=auth_headers(token),
        json={"items": [{"product_id": 1, "quantity": 99}]},
    )
    assert r.status_code == 409
    body = r.json()
    assert body["message"].startswith("Insufficient stock")
    assert body["errors"] is None

    # summary should still be empty (rollback worked)
    s = client.get("/reports/orders/summary", headers=auth_headers(token))
    assert s.status_code == 200
    assert s.json() == []


def test_get_order_detail_after_successful_order(client):
    token = login(client, "user@mail.com", "user1234")

    # buat 1 order
    r = client.post(
        "/orders",
        headers=auth_headers(token),
        json={"items": [{"product_id": 1, "quantity": 1}]},
    )
    assert r.status_code == 201, r.text
    order_id = r.json()["id"]

    d = client.get(f"/orders/{order_id}", headers=auth_headers(token))
    assert d.status_code == 200, d.text

    body = d.json()
    assert body["id"] == order_id
    assert body["total_items"] == 1
    assert body["total_amount"] == 250000
    assert len(body["items"]) == 1
    assert body["items"][0]["product_id"] == 1
    assert body["items"][0]["quantity"] == 1


def test_admin_can_see_all_order_summary(client):
    # user buat order dulu
    user_token = login(client, "user@mail.com", "user1234")
    r = client.post(
        "/orders",
        headers=auth_headers(user_token),
        json={"items": [{"product_id": 1, "quantity": 1}]},
    )
    assert r.status_code == 201

    # admin lihat semua summary
    admin_token = login(client, "admin@mail.com", "admin123")
    s = client.get(
        "/reports/orders/summary/all",
        headers=auth_headers(admin_token),
    )
    assert s.status_code == 200, s.text
    rows = s.json()
    assert len(rows) >= 1
    # minimal satu order yang barusan dibuat
    assert any(r["total_amount"] == 250000 for r in rows)


def test_non_admin_cannot_see_all_order_summary(client):
    token = login(client, "user@mail.com", "user1234")
    r = client.get(
        "/reports/orders/summary/all",
        headers=auth_headers(token),
    )
    assert r.status_code == 403
    body = r.json()
    assert body["message"] == "Forbidden"
    assert body["errors"] is None
