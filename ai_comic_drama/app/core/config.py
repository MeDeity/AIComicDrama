from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "AI Comic Drama API"
    debug: bool = False


@lru_cache
def get_settings() -> Settings:
    return Settings()
