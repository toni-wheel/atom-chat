# Описание таблицы базы данных

from sqlalchemy import Column, Integer, String, Boolean
from models.base import Base


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=True)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
