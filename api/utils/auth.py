from jose import jwt, JWTError
import crud.user as user_crud
from fastapi import HTTPException


# Конфигурация JWT
SECRET_KEY = "your_secret_key"  # Секретный ключ, лучше использовать безопасный метод генерации
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def get_user_from_token(token: str):
    try:
        # Расшифровка токена
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Неверный токен: имя пользователя не найдено")
        
        # Получаем пользователя по имени
        user = user_crud.read_user_by_username(username)
        if user is None:
            raise HTTPException(status_code=404, detail="Пользователь не найден")
        return username

    except JWTError:
        raise HTTPException(status_code=401, detail="Невалидный токен")
    

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2huX2RvZSIsImV4cCI6MTczMDE5NjYwOX0.BNcj4u39aqj0lteUq2pjNa4C9UOLUAyGXm0MYgsmMYY"
