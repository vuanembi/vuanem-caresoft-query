import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_URL: str = os.getenv("APP_URL", "")

    REDIS_HOST: str = os.getenv("REDIS_HOST", "")
    REDIS_PASSWORD: str = os.getenv("REDIS_PASSWORD", "")

    class Config:
        env_file = ".env"


settings = Settings()
