# Схемы для валидации данных

from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str
    completed: bool = False

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass

class TaskInDBBase(TaskBase):
    id: int

class Task(TaskInDBBase):
    pass

class TaskUpdateField(BaseModel):
    key: str
    new_value: str