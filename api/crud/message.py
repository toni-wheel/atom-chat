import models.message as message_model, schemas.message as message_schemas
from database import engine, db


# Создание сообщения
def create_message(message: message_schemas.MessageCreate):
    new_message = message_model.Message(**message.model_dump())
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    return new_message


# Получение всех сообщений с пагинацией
def read_messages(limit: int, offset: int):
    return db.query(message_model.Message).offset(offset).limit(limit).all()


# Получение сообщения по ID
def read_message(message_id: int):
    return db.query(message_model.Message).filter(message_model.Message.id == message_id).first()


# Обновление данных сообщения
def update_message(message_id: int, key: str, new_value):
    found_message = read_message(message_id)
    if found_message is None:
        return None
    if hasattr(found_message, key):
        setattr(found_message, key, new_value)
        db.commit()
        db.refresh(found_message)
        return found_message
    else:
        return None


# Удаление сообщения по ID
def delete_message(message_id: int):
    found_message = read_message(message_id)
    if found_message is None:
        return None
    db.delete(found_message)
    db.commit()
    return found_message


# Удаление всех сообщений
def delete_messages():
    found_messages = db.query(message_model.Message).all()
    if found_messages is None:
        return None
    for message in found_messages:
        db.delete(message)
    db.commit()
    return found_messages
