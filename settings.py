from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_URL: str

    REDIS_HOST: str
    REDIS_PASSWORD: str

    NS_ACCOUNT_ID: str
    NS_CONSUMER_KEY: str
    NS_CONSUMER_SECRET: str
    NS_ACCESS_TOKEN: str
    NS_TOKEN_SECRET: str
    NS_SUITETALK_URL: str
    NS_RESTLET_URL: str

    class Config:
        env_file = ".env"


settings = Settings()  # type: ignore
