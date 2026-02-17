from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POKEAPI_BASE_URL: str = "https://pokeapi.co/api/v2"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()