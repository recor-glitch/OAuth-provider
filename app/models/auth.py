from typing import List
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import func, ForeignKey, text, String, Integer, Boolean, DateTime
from datetime import datetime
from .base import BaseModel


class Oauth_client(BaseModel):
    __tablename__ = "oauth_clients"

    client_id: Mapped[str] = mapped_column(String, primary_key=True)
    client_secret: Mapped[str] = mapped_column(String)
    client_name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())
    redirect_uris: Mapped[dict] = mapped_column(JSONB(none_as_null=True), server_default=text("'{}'::jsonb"))

    created_by: Mapped[int] = mapped_column(ForeignKey("users.id"))
    organization_id: Mapped[int] = mapped_column(ForeignKey("organizations.id"))


class Authorization_code(BaseModel):
    __tablename__ = "authorization_codes"

    code: Mapped[str] = mapped_column(String, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now)
    client_id: Mapped[str] = mapped_column(String, ForeignKey("oauth_clients.client_id"))
    organization_id: Mapped[int] = mapped_column(Integer, ForeignKey("organizations.id"))
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    redirect_uri: Mapped[str] = mapped_column(String)
    expires_at: Mapped[datetime] = mapped_column(DateTime)


class Refresh_token(BaseModel):
    __tablename__ = "refresh_tokens"

    token_id: Mapped[str] = mapped_column(String, primary_key=True)
    client_id: Mapped[str] = mapped_column(String)
    token_hash: Mapped[str] = mapped_column(String)
    client_id: Mapped[str] = mapped_column(String)
    scope: Mapped[List[str]] = mapped_column(JSONB)
    expires_at: Mapped[datetime] = mapped_column(DateTime)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    organization_id: Mapped[int] = mapped_column(ForeignKey("organizations.id"))
