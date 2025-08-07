from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime

class Organization(DeclarativeBase):
    __tablename__ = "organizations"

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now)
    name: Mapped[str]
    description: Mapped[str]
    slug: Mapped[str] = mapped_column(unique=True)
    domain: Mapped[str] = mapped_column(unique=True)
    settings: Mapped[map] = mapped_column(default={})
    is_active: Mapped[bool] = mapped_column(default=True)