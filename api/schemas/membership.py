from pydantic import BaseModel
from datetime import datetime


# Базовая схема членства
class MembershipBase(BaseModel):
    user_id: int
    channel_id: int

# Схема для создания членства
class MembershipCreate(MembershipBase):
    pass

# Схема для вывода информации о членстве
class MembershipOut(MembershipBase):
    joined_at: datetime

    class Config:
        orm_mode = True

# Схема для обновления данных членства
class MembershipUpdate(BaseModel):
    joined_at: datetime = None  # Поля, которые могут быть изменены

    class Config:
        orm_mode = True