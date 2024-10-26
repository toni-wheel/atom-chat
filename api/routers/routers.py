# Маршруты для работы с задачами

from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated, List
from fake import fake_tasks, find_tasks
import crud.crud as crud, schemas.schemas as schemas

router = APIRouter(prefix="/tasks", tags=["tasks"])

# Создание задачи
@router.post("/")
def create_task(task: Annotated[schemas.TaskCreate, Depends()]):
    return crud.create_task(task)

# Получить данные всех задач
@router.get("/")
def read_tasks(limit: int = 5, offset: int = 0):
    return crud.read_tasks(limit, offset)

# Получение данных задачи по ID
@router.get("/{task_id}")
def read_task(task_id: int):
    found_task = crud.read_task(task_id)
    if found_task is None:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return found_task

# Обновление данных задачи
@router.patch("/{task_id}")
def update_task(task_id: int, field: Annotated[schemas.TaskUpdateField, Depends()]):
    found_task = crud.update_task(task_id, key=field.key, new_value=field.new_value)
    if found_task is None:
        raise HTTPException(status_code=404, detail="Задача не найдена или неверный формат данных")

# Удаление задачи по ID
@router.delete("/{task_id}")
def delete_task(task_id: int):
    return crud.delete_task(task_id)

# Удаление всех задач
@router.delete("/")
def delete_tasks():
    found_tasks = crud.delete_tasks()
    if found_tasks is None:
        raise HTTPException(status_code=404, detail="Задачи не найдены")
    return found_tasks