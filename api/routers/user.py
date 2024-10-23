# Маршруты для работы с пользователями

from fastapi import APIRouter, Depends, HTTPException

from typing import Annotated
import crud.user as user_crud
import schemas.user as user_schemas


user_router = APIRouter(prefix="/user", tags=["user"])


# Создание пользователя
@user_router.post("/")
def create_user(user: Annotated[user_schemas.UserCreate, Depends()]):
    return user_crud.create_user(user)


# Регистрация пользователя
@user_router.post("/register")
def register_user(user: Annotated[user_schemas.UserCreate, Depends()]):
    return user_crud.register_user(user)


# Авторизация пользователя
@user_router.post("/login")
def login(user: Annotated[user_schemas.UserLogin, Depends()]):
    return user_crud.login(user)


# Получить данных всех пользователей
@user_router.get("/")
def read_users(limit: int = 5, offset: int = 0):
    return user_crud.read_users(limit, offset)


# Получение данных пользователя по ID
@user_router.get("/{user_id}")
def read_user(user_id: int):
    found_user = user_crud.read_user(user_id)
    if found_user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найдена")
    return found_user


# Обновление данных пользователя
@user_router.patch("/{user_id}")
def update_user(user_id: int, field: Annotated[user_schemas.UserUpdateField, Depends()]):
    found_user = user_crud.update_user(user_id, key=field.key, new_value=field.new_value)
    if found_user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден или неверный формат данных")


# Удаление пользователя по ID
@user_router.delete("/{user_id}")
def delete_user(user_id: int):
    return user_crud.delete_user(user_id)


# Удаление всех пользователей
@user_router.delete("/")
def delete_users():
    found_users = user_crud.delete_users()
    if found_users is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return found_users