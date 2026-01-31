from fastapi import FastAPI, HTTPException, Request

app = FastAPI(title="Simple User CRUD (No DB, No Pydantic)")

db = {}       # {id: user_dict}
next_id = 1   # auto increment


def get_user_or_404(user_id: int):
  user = db.get(user_id)
  if not user:
    raise HTTPException(status_code=404, detail="User not found")
  return user


@app.get("/")
def root():
  return {"ok": True, "docs": "/docs"}


# CREATE
@app.post("/users", status_code=201)
async def create_user(request: Request):
  global next_id
  data = await request.json()

  # super basic manual validation
  name = str(data.get("name", "")).strip()
  email = str(data.get("email", "")).strip()

  if not name:
    raise HTTPException(status_code=422, detail="name is required")
  if not email:
    raise HTTPException(status_code=422, detail="email is required")

  # simple uniqueness check
  for u in db.values():
    if u["email"].lower() == email.lower():
      raise HTTPException(status_code=409, detail="email already used")

  user = {
    "id": next_id,
    "name": name,
    "email": email,
    "is_active": bool(data.get("is_active", True)),
  }

  db[next_id] = user
  next_id += 1
  return user


# READ ALL
@app.get("/users")
def list_users():
  return list(db.values())


# READ ONE
@app.get("/users/{user_id}")
def get_user(user_id: int):
  return get_user_or_404(user_id)


# UPDATE (replace) - PUT
@app.put("/users/{user_id}")
async def replace_user(user_id: int, request: Request):
  user = get_user_or_404(user_id)
  data = await request.json()

  name = str(data.get("name", "")).strip()
  email = str(data.get("email", "")).strip()

  if not name:
    raise HTTPException(status_code=422, detail="name is required")
  if not email:
    raise HTTPException(status_code=422, detail="email is required")

  # uniqueness check (exclude current user)
  for uid, u in db.items():
    if uid != user_id and u["email"].lower() == email.lower():
      raise HTTPException(status_code=409, detail="email already used")

  user = {
    "id": user_id,
    "name": name,
    "email": email,
    "is_active": bool(data.get("is_active", True)),
  }
  db[user_id] = user
  return user


# UPDATE (partial) - PATCH
@app.patch("/users/{user_id}")
async def update_user(user_id: int, request: Request):
  user = get_user_or_404(user_id)
  data = await request.json()

  if "name" in data:
    name = str(data["name"]).strip()
    if not name:
      raise HTTPException(status_code=422, detail="name cannot be empty")
    user["name"] = name

  if "email" in data:
    email = str(data["email"]).strip()
    if not email:
      raise HTTPException(status_code=422, detail="email cannot be empty")

    for uid, u in db.items():
      if uid != user_id and u["email"].lower() == email.lower():
        raise HTTPException(status_code=409, detail="email already used")

    user["email"] = email

  if "is_active" in data:
    user["is_active"] = bool(data["is_active"])

  db[user_id] = user
  return user


# DELETE
@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int):
  _ = get_user_or_404(user_id)
  del db[user_id]
  return None
