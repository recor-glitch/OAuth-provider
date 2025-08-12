from pydantic import BaseModel, Field
from datetime import datetime


class UserBase(BaseModel):
    email: str = Field()
    password: str
    first_name: str
    last_name: str

class UserCreate(UserBase):
    password: str

class UserPublic(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

class UserUpdate(BaseModel):
    email: str | None = None
    password: str | None = None
    first_name: str | None = None
    last_name: str | None = None

