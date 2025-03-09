from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL_FASTAPI: str
    DEBUG: bool = False
    BASE_BACKEND_URL: str
    BACKEND_LOGIN_URL: str
    REDIS_HOST: str
    REDIS_PORT: int

    class Config:
        env_file = ".env"


settings = Settings()
