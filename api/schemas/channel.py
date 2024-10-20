from pydantic import BaseModel
from datetime import datetime


class ChannelBase(BaseModel):
    name: str

class ChannelCreate(ChannelBase):
    pass

class ChannelOut(ChannelBase):
    id: int
    is_private: bool
    created_at: datetime

    class Config:
        orm_mode = True