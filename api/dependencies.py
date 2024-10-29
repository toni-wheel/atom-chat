from fastapi import Depends, HTTPException
from utils.auth import get_user_from_token  # Функция для извлечения пользователя из токена
import models.user as user_models
import crud.user as user_crud


# Проверка, что пользователь является модератором
async def moderator_only(current_user_name: user_models.User = Depends(get_user_from_token)):
    current_user = user_crud.read_user_by_username(current_user_name)
    if not current_user.is_moderator:
        raise HTTPException(status_code=403, detail="Доступ запрещен. Только модератор может блокировать пользователей.")
    return current_user

