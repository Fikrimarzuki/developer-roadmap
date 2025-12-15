import json
import os
from fastapi import FastAPI, HTTPException, Body

app = FastAPI(title="User CRUD (JSON DB)")

DB_PATH = "db.json"

def load_users():
  if not os.path.exists(DB_PATH):
    return []

  try:
    with open(DB_PATH, "r", encoding="utf-8") as f:
      data = json.load(f)
      return data if isinstance(data, list) else []
  except json.JSONDecodeError:
    return []


def save_users(users):
  with open(DB_PATH, "w", encoding="utf-8") as f:
      json.dump(users, f, ensure_ascii=False, indent=2)


def get_next_id(users):
  if not users:
    return 1
  return max(u.get("id", 0) for u in users) + 1


def find_user(users, user_id: int):
  for u in users:
    if u.get("id") == user_id:
      return u
  return None


# ROUTE
@app.get("/")
def root():
  return {"ok": True, "docs": "/docs"}


@app.post("/users", status_code=201)
def create_user(
  data: dict = Body(
    ...,
    example={"name": "Python", "email": "python@mail.com", "is_active": True},
  )
):
  users = load_users()

  name = str(data.get("name", "")).strip()
  email = str(data.get("email", "")).strip()

  if not name:
    raise HTTPException(status_code=422, detail="name is required")
  if not email:
    raise HTTPException(status_code=422, detail="email is required")

  for u in users:
    if str(u.get("email", "")).lower() == email.lower():
      raise HTTPException(status_code=409, detail="email already used")

  user = {
    "id": get_next_id(users),
    "name": name,
    "email": email,
    "is_active": bool(data.get("is_active", True)),
  }

  users.append(user)
  save_users(users)
  return user


@app.get("/users")
def list_users():
  return load_users()


@app.get("/users/{user_id}")
def get_user(user_id: int):
  users = load_users()
  user = find_user(users, user_id)
  if not user:
    raise HTTPException(status_code=404, detail="User not found")
  return user


@app.put("/users/{user_id}")
def replace_user(
  user_id: int,
  data: dict = Body(
    ...,
    example={"name": "Updated", "email": "updated@mail.com", "is_active": True},
  )
):
  users = load_users()
  user = find_user(users, user_id)

  if not user:
    raise HTTPException(status_code=404, detail="User not found")

  name = str(data.get("name", "")).strip()
  email = str(data.get("email", "")).strip()

  if not name:
    raise HTTPException(status_code=422, detail="name is required")
  if not email:
    raise HTTPException(status_code=422, detail="email is required")

  for u in users:
    if u.get("id") != user_id and str(u.get("email", "")).lower() == email.lower():
      raise HTTPException(status_code=409, detail="email already used")

  user["name"] = name
  user["email"] = email
  user["is_active"] = bool(data.get("is_active", True))

  save_users(users)
  return user


# UPDATE (partial) - PATCH
@app.patch("/users/{user_id}")
def update_user(
  user_id: int,
  data: dict = Body(
    ...,
    example={"name": "Partial Update", "is_active": False},
  )
):
  users = load_users()
  user = find_user(users, user_id)

  if not user:
    raise HTTPException(status_code=404, detail="User not found")

  if "name" in data:
    name = str(data["name"]).strip()
    if not name:
      raise HTTPException(status_code=422, detail="name cannot be empty")
    user["name"] = name

  if "email" in data:
    email = str(data["email"]).strip()
    if not email:
      raise HTTPException(status_code=422, detail="email cannot be empty")

    for u in users:
      if u.get("id") != user_id and str(u.get("email", "")).lower() == email.lower():
        raise HTTPException(status_code=409, detail="email already used")

    user["email"] = email

  if "is_active" in data:
    user["is_active"] = bool(data["is_active"])

  save_users(users)
  return user


@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int):
  users = load_users()
  user = find_user(users, user_id)

  if not user:
    raise HTTPException(status_code=404, detail="User not found")

  users.remove(user)
  save_users(users)
  return None















