import models.channel as channel_model, schemas.channel as channel_schemas
from database import engine, db


# Создание канала
def create_channel(channel: channel_schemas.ChannelCreate):
    new_channel = channel_model.Channel(**channel.model_dump())
    db.add(new_channel)
    db.commit()
    db.refresh(new_channel)
    return new_channel


# Получение всех каналов с пагинацией
def read_channels(limit: int, offset: int):
    return db.query(channel_model.Channel).offset(offset).limit(limit).all()


# Получение канала по ID
def read_channel(channel_id: int):
    return db.query(channel_model.Channel).filter(channel_model.Channel.id == channel_id).first()


# Обновление данных канала
def update_channel(channel_id: int, key: str, new_value):
    found_channel = read_channel(channel_id)
    if found_channel is None:
        return None
    if hasattr(found_channel, key):
        setattr(found_channel, key, new_value)
        db.commit()
        db.refresh(found_channel)
        return found_channel
    else:
        return None


# Удаление канала по ID
def delete_channel(channel_id: int):
    found_channel = read_channel(channel_id)
    if found_channel is None:
        return None
    db.delete(found_channel)
    db.commit()
    return found_channel


# Удаление всех каналов
def delete_channels():
    found_channels = db.query(channel_model.Channel).all()
    if found_channels is None:
        return None
    for channel in found_channels:
        db.delete(channel)
    db.commit()
    return found_channels
