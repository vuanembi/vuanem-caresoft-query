from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    user_id: str
    phone: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime

    class Config:
        orm_mode = True
