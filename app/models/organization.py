from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import ENUM, JSONB
from sqlalchemy import ForeignKey, text, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from datetime import datetime

from .base import BaseModel
from enum import Enum

class Organization(BaseModel):
    __tablename__ = "organizations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())
    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(100))
    slug: Mapped[str] = mapped_column(String, unique=True)
    domain: Mapped[str] = mapped_column(String, unique=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    settings: Mapped[dict] = mapped_column(JSONB(none_as_null=True), server_default=text("'{}'::jsonb"))

    users: Mapped[List["User_Organization"]] = relationship("User_Organization", back_populates="organization")


class Role_enum(Enum):
    ADMIN="admin"
    MEMBER="member"
    GUEST="guest"

class User_Organization(BaseModel):
    __tablename__ = "users_organizations"

    organization_id: Mapped[int] = mapped_column(Integer, ForeignKey("organizations.id"), primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    invited_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    invited_by: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    role: Mapped[Role_enum] = mapped_column(ENUM(Role_enum, name="organization_user_role", create_type=False), default=Role_enum.MEMBER)

    user: Mapped["User"] = relationship("User", foreign_keys=[user_id], back_populates="organizations")
    organization: Mapped["Organization"] = relationship("Organization", foreign_keys=[organization_id], back_populates="users")
    invited_by_user: Mapped["User"] = relationship("User", foreign_keys=[invited_by])