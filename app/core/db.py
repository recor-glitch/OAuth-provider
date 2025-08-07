from sqlalchemy import create_engine
from app.core.setttings import setting
from sqlalchemy.orm import sessionmaker


engine = create_engine(setting.DATABASE_URL)

sessionLocal = sessionmaker(bind=engine, autoflush=False)


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()