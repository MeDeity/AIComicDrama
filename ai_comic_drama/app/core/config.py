from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "AI Comic Drama API"
    debug: bool = False
    llm_provider: str = "dummy"
    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "qwen3:30b"
    glm_base_url: str | None = None
    glm_api_key: str | None = None


@lru_cache
def get_settings() -> Settings:
    return Settings()
