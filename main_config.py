from pydantic_settings import BaseSettings


class MainSettings(BaseSettings):
    BASE_BACKEND_URL: str
    BASE_MICROSERVICE_URL: str

    class Config:
        env_file = ".env"


main_settings = MainSettings()
