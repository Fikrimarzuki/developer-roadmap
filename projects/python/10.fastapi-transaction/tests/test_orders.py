from tests.helpers import login, auth_headers

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
