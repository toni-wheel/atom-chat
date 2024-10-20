from pydantic import BaseModel
from datetime import datetime


class MembershipBase(BaseModel):
    user_id: int
    channel_id: int

class MembershipOut(MembershipBase):
    joined_at: datetime

    class Config:
        orm_mode = True