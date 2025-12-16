import json, os

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
