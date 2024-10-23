from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    password: str


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class UserInDBBase(UserBase):
    id: int


class User(UserInDBBase):
    pass


class UserUpdateField(BaseModel):
    key: str
    new_value: str


class UserLogin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


# class UserBase(BaseModel):
#     username: str
#     email: str

# class UserCreate(UserBase):
#     password: str

# class UserOut(UserBase):
#     id: int
#     is_moderator: bool
#     is_active: bool

#     class Config:
#         orm_mode = True