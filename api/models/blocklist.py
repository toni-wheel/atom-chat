from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base  # Импортируем базовый класс для моделей

class BlockList(Base):
    __tablename__ = "blocklist"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    blocked_by = Column(Integer, ForeignKey("users.id"))
    blocked_at = Column(DateTime(timezone=True), server_default=func.now())

    blocked_by_user = relationship("User", back_populates="blocked_users", foreign_keys=[blocked_by])