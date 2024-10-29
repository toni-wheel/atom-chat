from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    password: str
    is_moderator: bool
    is_active: bool


class UserCreate(UserBase):
    pass


class UserUpdateField(BaseModel):
    key: str
    new_value: str


class UserInDBBase(UserBase):
    id: int

    class Config:
        orm_mode = True


class User(UserInDBBase):
    pass


class UserLogin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str