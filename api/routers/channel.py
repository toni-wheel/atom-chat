from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated, List
import crud.channel as channel_crud, schemas.channel as channel_schemas


channel_router = APIRouter(prefix="/channels", tags=["channels"])


# Создание канала
@channel_router.post("/", response_model=channel_schemas.ChannelOut)
def create_channel(channel: Annotated[channel_schemas.ChannelCreate, Depends()]):
    return channel_crud.create_channel(channel)


# Получить данные всех каналов
@channel_router.get("/", response_model=List[channel_schemas.ChannelOut])
def read_channels(limit: int = 5, offset: int = 0):
    return channel_crud.read_channels(limit, offset)


# Получение данных канала по ID
@channel_router.get("/{channel_id}", response_model=channel_schemas.ChannelOut)
def read_channel(channel_id: int):
    found_channel = channel_crud.read_channel(channel_id)
    if found_channel is None:
        raise HTTPException(status_code=404, detail="Канал не найден")
    return found_channel


# Обновление данных канала
@channel_router.patch("/{channel_id}")
def update_channel(channel_id: int, field: Annotated[channel_schemas.ChannelUpdateField, Depends()]):
    updated_channel = channel_crud.update_channel(channel_id, key=field.key, new_value=field.new_value)
    if updated_channel is None:
        raise HTTPException(status_code=404, detail="Канал не найден или неверный формат данных")
    return updated_channel


# Удаление канала по ID
@channel_router.delete("/{channel_id}")
def delete_channel(channel_id: int):
    deleted_channel = channel_crud.delete_channel(channel_id)
    if deleted_channel is None:
        raise HTTPException(status_code=404, detail="Канал не найден")
    return deleted_channel


# Удаление всех каналов
@channel_router.delete("/")
def delete_channels():
    deleted_channels = channel_crud.delete_channels()
    if deleted_channels is None:
        raise HTTPException(status_code=404, detail="Каналы не найдены")
    return deleted_channels
