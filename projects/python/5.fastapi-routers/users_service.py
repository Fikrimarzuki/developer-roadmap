from fastapi import HTTPException
from json_db import load_users, save_users, get_next_id, find_user

def create_user(data: dict):
  users = load_users()

  name = str(data.get("name", "")).strip()
  email = str(data.get("email", "")).strip()

  if not name:
    raise HTTPException(status_code=422, detail="name is required")
  if not email:
    raise HTTPException(status_code=422, detail="email is required")

  for u in users:
    if str(u.get("email","")).lower() == email.lower():
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

def list_users():
  return load_users()

def get_user(user_id: int):
  users = load_users()
  user = find_user(users, user_id)

  if not user:
    raise HTTPException(status_code=404, detail="User not found")
  return user

def replace_user(user_id: int, data: dict):
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
    if u.get("id") != user_id and str(u.get("email","")).lower() == email.lower():
      raise HTTPException(status_code=409, detail="email already used")

  user["name"] = name
  user["email"] = email
  user["is_active"] = bool(data.get("is_active", True))

  save_users(users)
  return user

def update_user(user_id: int, data: dict):
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
      if u.get("id") != user_id and str(u.get("email","")).lower() == email.lower():
        raise HTTPException(status_code=409, detail="email already used")

    user["email"] = email

  if "is_active" in data:
    user["is_active"] = bool(data["is_active"])

  save_users(users)
  return user

def delete_user(user_id: int):
  users = load_users()
  user = find_user(users, user_id)
  
  if not user:
    raise HTTPException(status_code=404, detail="User not found")

  users.remove(user)
  save_users(users)
