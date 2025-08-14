from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class OrganizationBase(BaseModel):
    name: str
    description: str
    slug: str
    domain: str


class OrganizationCreate(OrganizationBase):
    settings: Optional[dict] = None

class OrganizationPublic(OrganizationBase):
    id: int
    is_active: bool
    settings: dict
    created_at: datetime
    updated_at: datetime
    users: list

class OrganizationUpdate(OrganizationBase):
    name: Optional[str] = None
    description: Optional[str] = None
    slug: Optional[str] = None
    domain: Optional[str] = None
    settings: Optional[dict] = None
    is_active: Optional[bool] = None
    users: Optional[list] = None