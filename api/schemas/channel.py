from pydantic import BaseModel
from datetime import datetime


class ChannelBase(BaseModel):
    name: str


class ChannelCreate(ChannelBase):
    pass


class ChannelUpdateField(BaseModel):
    key: str
    new_value: str


class ChannelOut(ChannelBase):
    id: int
    is_private: bool
    created_at: datetime

    class Config:
        orm_mode = True