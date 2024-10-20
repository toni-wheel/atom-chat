from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from database import Base  # Импортируем базовый класс для моделей

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_moderator = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    
    messages = relationship("Message", back_populates="user")
    memberships = relationship("Membership", back_populates="user")
    blocked_users = relationship("BlockList", back_populates="blocked_by_user", foreign_keys="[BlockList.blocked_by]")