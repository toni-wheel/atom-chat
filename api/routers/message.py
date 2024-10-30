from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated, List
import crud.message as message_crud, schemas.message as message_schemas
import models.user as user_models


message_router = APIRouter(prefix="/messages", tags=["messages"])


# Создание сообщения
@message_router.post("/", response_model=message_schemas.MessageOut)
async def create_message(message: Annotated[message_schemas.MessageCreate, Depends()]):
    new_message = await message_crud.create_message(message)
    return new_message


# Получить данные всех сообщений
@message_router.get("/", response_model=List[message_schemas.MessageOut])
def read_messages(limit: int = 5, offset: int = 0):
    return message_crud.read_messages(limit, offset)


# Получение данных сообщения по ID
@message_router.get("/{message_id}", response_model=message_schemas.MessageOut)
def read_message(message_id: int):
    found_message = message_crud.read_message(message_id)
    if found_message is None:
        raise HTTPException(status_code=404, detail="Сообщение не найдено")
    return found_message


# Получение сообщений по channel_id
@message_router.get("/channel/{channel_id}", response_model=List[message_schemas.MessageOut])
def read_messages_by_channel(channel_id: int, limit: int = 5, offset: int = 0):
    messages = message_crud.read_messages_by_channel(channel_id, limit, offset)
    # if not messages:
    #     raise HTTPException(status_code=404, detail="Сообщения не найдены для данного канала")
    return messages


# Обновление данных сообщения
@message_router.patch("/{message_id}")
def update_message(message_id: int, field: Annotated[message_schemas.MessageUpdateField, Depends()]):
    updated_message = message_crud.update_message(message_id, key=field.key, new_value=field.new_value)
    if updated_message is None:
        raise HTTPException(status_code=404, detail="Сообщение не найдено или неверный формат данных")
    return updated_message


# Удаление сообщения по ID
@message_router.delete("/{message_id}")
def delete_message(message_id: int):
    deleted_message = message_crud.delete_message(message_id)
    if deleted_message is None:
        raise HTTPException(status_code=404, detail="Сообщение не найдено")
    return deleted_message


# Удаление всех сообщений
@message_router.delete("/")
def delete_messages():
    deleted_messages = message_crud.delete_messages()
    if deleted_messages is None:
        raise HTTPException(status_code=404, detail="Сообщения не найдены")
    return deleted_messages
