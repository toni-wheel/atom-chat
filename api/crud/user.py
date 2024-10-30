# Взаимодействие с таблицей пользователей в БД

from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from database import engine, db
from passlib.context import CryptContext
from utils.jwt import create_access_token
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


# Регистрация пользователя
def register_user(user: user_schemas.UserCreate):
    # Проверяем, существует ли пользователь username
    user_exists = db.query(user_models.User).filter(user_models.User.username == user.username).first()
    if user_exists:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Такой пользователь уже существует!")
    new_user = user_models.User(
        username=user.username,
        password=get_password_hash(user.password),
        is_moderator=user.is_moderator,
        is_active=user.is_active
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return JSONResponse(content={"message": "Пользователь успешно зарегистрирован!"}, status_code=status.HTTP_201_CREATED)



# Авторизация пользователя
def authenticate_user(username: str, password: str):
    user = db.query(user_models.User).filter(user_models.User.username == username).first()
    if user and verify_password(password, user.password):
        return user
    return None


def login(user: user_schemas.UserLogin):
    # Проверка подлинности пользователя
    user = authenticate_user(user.username, user.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Неправильное имя пользователя или пароль")
    if not user.is_active:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Ваш аккаунт заблокирован.")
    
    # Создаем токен доступа
    access_token = create_access_token(data={"sub": user.username})
    
    # Возвращаем JSON-ответ с токеном и данными пользователя
    return JSONResponse(
        content={"user": {"id": user.id, "username": user.username, "is_moderator": user.is_moderator}, "access_token": access_token, "token_type": "bearer"},
        status_code=status.HTTP_200_OK
    )


# Получить данных всех пользователей
def read_users(limit: int, offset: int):
    return db.query(user_models.User).offset(offset).limit(limit).all()


# Получение данных пользователя по ID
def read_user(user_id: int):
    return db.query(user_models.User).filter(user_models.User.id == user_id).first()


# Получение данных пользователя по имени пользователя
def read_user_by_username(username: str):
    user = db.query(user_models.User).filter(user_models.User.username == username).first()
    if user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return user


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


# Блокировка пользователя
def block_user(user_id: int):
    user = read_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    user.is_active = False
    db.commit()
    print(user.is_active)
    return user

