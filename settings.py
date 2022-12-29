import os

import dotenv
from pydantic import BaseSettings

dotenv.load_dotenv()


class Settings:
    APP_URL: str = os.getenv("APP_URL", "")

    DB_URL: str = os.getenv("DB_URL", "")

    REDIS_HOST: str = os.getenv("REDIS_HOST", "")
    REDIS_PASSWORD: str = os.getenv("REDIS_PASSWORD", "")

    ZALO_CLIENT_ID: str = "533162694613946571"
    ZALO_CLIENT_SECRET: str = os.getenv("ZALO_CLIENT_SECRET", "")


settings = Settings()
