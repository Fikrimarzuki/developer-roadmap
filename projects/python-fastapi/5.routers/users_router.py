from fastapi import APIRouter, Body
from users_service import (
  create_user,
  list_users,
  get_user,
  replace_user,
  update_user,
  delete_user
)

router = APIRouter(prefix="/users", tags=["users"])

@router.post("", status_code=201)
def create(
  data: dict = Body(
    ...,
    example={"name":"Python","email":"python@mail.com","is_active":True}
  )
):
  return create_user(data)

@router.get("")
def list_all():
  return list_users()

@router.get("/{user_id}")
def get_one(user_id: int):
  return get_user(user_id)

@router.put("/{user_id}")
def put(
  user_id: int,
  data: dict = Body(
    ...,
    example={"name":"Updated","email":"updated@mail.com","is_active":True}
  )
):
  return replace_user(user_id, data)

@router.patch("/{user_id}")
def patch(
  user_id: int,
  data: dict = Body(
    ...,
    example={"is_active":False}
  )
):
  return update_user(user_id, data)

@router.delete("/{user_id}", status_code=204)
def remove(user_id: int):
  delete_user(user_id)
  return None



