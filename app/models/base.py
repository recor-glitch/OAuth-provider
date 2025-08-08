from app.core.db import Base


class BaseModel(Base):
    __abstract__ = True
    pass