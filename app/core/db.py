from app.core.setttings import setting
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base


engine = create_async_engine(setting.DATABASE_URL)

async_session_local = async_sessionmaker(bind=engine, autoflush=False, class_=AsyncSession, expire_on_commit=False)


Base = declarative_base()


async def get_db():
    async with async_session_local as session:
        try:
            yield session
        finally:
            await session.close()