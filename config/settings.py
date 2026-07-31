from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Enterprise Healthcare Information System"
    APP_VERSION: str = "1.0.0"


    DATABASE_URL: str

    SECRET_KEY: str

    ALGORITHM: str

    ACCESS_TOKEN_EXPIRE_MINUTES: int

    REFRESH_TOKEN_EXPIRE_DAYS: int

    ENCRYPTION_KEY: str

    class Config:

        env_file = ".env"


settings = Settings()