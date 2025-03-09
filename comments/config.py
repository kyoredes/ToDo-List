from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = False
    REDIS_HOST: str
    REDIS_PORT: int

    class Config:
        env_file = ".env"


settings = Settings()
