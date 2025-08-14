from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime


class UserBase(BaseModel):
    email: str = Field(pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    first_name: str
    last_name: str

class UserCreate(UserBase):
    password: str

class UserPublic(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

class UserUpdate(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None

