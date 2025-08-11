from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class Create_Organization(BaseModel):
    name: str
    description: str
    slug: str
    domain: str
    settings: Optional[dict]


class Organization_User_Response(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime
    name: str
    description: str
    slug: str
    domain: str
    is_active: bool
    settings: dict | None
    users: list