from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding='utf-8')

    DATABASE_URL: str ="postgresql+asyncpg://user:password@postgres:5432/oauth?sslmode=disable"
    DATABASE_SYNC_URL: str ="postgresql://user:password@postgres:5432/oauth?sslmode=disable"

setting = Settings()