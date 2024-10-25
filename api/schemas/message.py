from pydantic import BaseModel
from datetime import datetime


class MessageBase(BaseModel):
    content: str


class MessageCreate(MessageBase):
    channel_id: int
    user_id: int


class MessageUpdateField(BaseModel):
    key: str
    new_value: str


class MessageOut(MessageBase):
    id: int
    channel_id: int
    user_id: int
    created_at: datetime


    class Config:
        orm_mode = True