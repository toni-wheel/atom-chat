from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated, List
import api.crud.crud as crud, api.schemas.schemas as schemas

router = APIRouter(prefix="/messages", tags=["messages"])

# Создание сообщения
@router.post("/", response_model=schemas.MessageOut)
def create_message(message: Annotated[schemas.MessageCreate, Depends()]):
    return crud.create_message(message)

# Получить данные всех сообщений
@router.get("/", response_model=List[schemas.MessageOut])
def read_messages(limit: int = 5, offset: int = 0):
    return crud.read_messages(limit, offset)

# Получение данных сообщения по ID
@router.get("/{message_id}", response_model=schemas.MessageOut)
def read_message(message_id: int):
    found_message = crud.read_message(message_id)
    if found_message is None:
        raise HTTPException(status_code=404, detail="Сообщение не найдено")
    return found_message

# Обновление данных сообщения
@router.patch("/{message_id}")
def update_message(message_id: int, field: Annotated[schemas.MessageUpdateField, Depends()]):
    updated_message = crud.update_message(message_id, key=field.key, new_value=field.new_value)
    if updated_message is None:
        raise HTTPException(status_code=404, detail="Сообщение не найдено или неверный формат данных")
    return updated_message

# Удаление сообщения по ID
@router.delete("/{message_id}")
def delete_message(message_id: int):
    deleted_message = crud.delete_message(message_id)
    if deleted_message is None:
        raise HTTPException(status_code=404, detail="Сообщение не найдено")
    return deleted_message

# Удаление всех сообщений
@router.delete("/")
def delete_messages():
    deleted_messages = crud.delete_messages()
    if deleted_messages is None:
        raise HTTPException(status_code=404, detail="Сообщения не найдены")
    return deleted_messages
