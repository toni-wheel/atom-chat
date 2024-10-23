# Функции для взаимодействия с базой данных

import api.models.models as models, api.schemas.schemas as schemas
from database import engine, db

def start():
    models.Base.metadata.create_all(engine)

def drop():
    models.Base.metadata.drop_all(engine)

def create_task(task: schemas.TaskCreate):
    new_task = models.Task(**task.model_dump())
    db.add(new_task)
    db.commit()
    return new_task

def read_tasks(limit: int, offset: int):
    return db.query(models.Task).offset(offset).limit(limit).all()

def read_task(task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def update_task(task_id: int, key: str, new_value):
    found_task = read_task(task_id)
    if found_task is None:
        return None
    if hasattr(found_task, key):
        setattr(found_task, key, new_value)
        db.commit()
        db.refresh(found_task)
        return found_task
    else:
        return None

def delete_task(task_id: int):
    found_task = read_task(task_id)
    if found_task is None:
        return None
    db.delete(found_task)
    db.commit()
    return found_task

def delete_tasks():
    found_tasks = db.query(models.Task).all()
    if found_tasks is None:
        return None
    for task in found_tasks:
        db.delete(task)
    db.commit()
    return found_tasks


