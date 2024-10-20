from pydantic import BaseModel
from datetime import datetime


class BlockListBase(BaseModel):
    user_id: int
    blocked_by: int

class BlockListOut(BlockListBase):
    blocked_at: datetime

    class Config:
        orm_mode = True