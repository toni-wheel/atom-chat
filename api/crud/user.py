# Взаимодействие с таблицей пользователей в БД

from fastapi import HTTPException
from database import engine, db
from passlib.context import CryptContext
from jwt import create_access_token
import schemas.user as user_schemas
import models.user as user_models

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def start():
    user_models.Base.metadata.create_all(engine)


def drop():
    user_models.Base.metadata.drop_all(engine)


# Создание пользователя
def create_user(user: user_schemas.UserCreate):
    new_user = user_models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    return new_user


# Регистрация пользователя
def register_user(user: user_schemas.UserCreate):
    # Проверяем, существует ли пользователь username
    user_exists = db.query(user_models.User).filter(user_models.User.username == user.username).first()
    if user_exists:
        raise HTTPException(status_code=400, detail="Такой пользователь уже существует!")
    new_user = user_models.User(
        username=user.username,
        password=get_password_hash(user.password)
    )
    db.add(new_user)
    db.commit()
    return new_user


# Авторизация пользователя
def authenticate_user(username: str, password: str):
    user = db.query(user_models.User).filter(user_models.User.username == username).first()
    if user and verify_password(password, user.password):
        return user
    return None


def login(user: user_schemas.UserLogin):
    user = authenticate_user(user.username, user.password)
    if not user:
        raise HTTPException(status_code=400, detail="Неправильное имя пользователя или пароль")
    
    access_token = create_access_token(data={"sub": user.username})
    return {"user": user, "access_token": access_token, "token_type": "bearer"}


# Получить данных всех пользователей
def read_users(limit: int, offset: int):
    return db.query(user_models.User).offset(offset).limit(limit).all()


# Получение данных пользователя по ID
def read_user(user_id: int):
    return db.query(user_models.User).filter(user_models.User.id == user_id).first()


# Обновление данных пользователя
def update_user(user_id: int, key: str, new_value):
    found_user = read_user(user_id)
    if found_user is None:
        return None
    if hasattr(found_user, key):
        setattr(found_user, key, new_value)
        db.commit()
        db.refresh(found_user)
        return found_user
    else:
        return None


# Удаление пользователя по ID
def delete_user(user_id: int):
    found_user = read_user(user_id)
    if found_user is None:
        return None
    db.delete(found_user)
    db.commit()
    return found_user


# Удаление всех пользователей
def delete_users():
    found_users = db.query(user_models.User).all()
    if found_users is None:
        return None
    for user in found_users:
        db.delete(user)
    db.commit()
    return found_users


