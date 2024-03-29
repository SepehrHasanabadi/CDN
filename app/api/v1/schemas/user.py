from pydantic import BaseModel


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    class Config:
        orm_mode = True


class UserCredential(UserBase):
    password: str

    class Config:
        orm_mode = True
