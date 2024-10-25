from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated, List
import api.crud.crud as crud, api.schemas.schemas as schemas

router = APIRouter(prefix="/channels", tags=["channels"])

# Создание канала
@router.post("/", response_model=schemas.ChannelOut)
def create_channel(channel: Annotated[schemas.ChannelCreate, Depends()]):
    return crud.create_channel(channel)

# Получить данные всех каналов
@router.get("/", response_model=List[schemas.ChannelOut])
def read_channels(limit: int = 5, offset: int = 0):
    return crud.read_channels(limit, offset)

# Получение данных канала по ID
@router.get("/{channel_id}", response_model=schemas.ChannelOut)
def read_channel(channel_id: int):
    found_channel = crud.read_channel(channel_id)
    if found_channel is None:
        raise HTTPException(status_code=404, detail="Канал не найден")
    return found_channel

# Обновление данных канала
@router.patch("/{channel_id}")
def update_channel(channel_id: int, field: Annotated[schemas.ChannelUpdateField, Depends()]):
    updated_channel = crud.update_channel(channel_id, key=field.key, new_value=field.new_value)
    if updated_channel is None:
        raise HTTPException(status_code=404, detail="Канал не найден или неверный формат данных")
    return updated_channel

# Удаление канала по ID
@router.delete("/{channel_id}")
def delete_channel(channel_id: int):
    deleted_channel = crud.delete_channel(channel_id)
    if deleted_channel is None:
        raise HTTPException(status_code=404, detail="Канал не найден")
    return deleted_channel

# Удаление всех каналов
@router.delete("/")
def delete_channels():
    deleted_channels = crud.delete_channels()
    if deleted_channels is None:
        raise HTTPException(status_code=404, detail="Каналы не найдены")
    return deleted_channels
