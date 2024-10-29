from datetime import datetime, timedelta, timezone
from jose import jwt


# Конфигурация JWT
SECRET_KEY = "your_secret_key"  # Секретный ключ, лучше использовать безопасный метод генерации
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


