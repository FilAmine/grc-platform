from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_env: str = "local"
    app_name: str = "GRC Platform"
    api_v1_prefix: str = "/api/v1"
    secret_key: str = Field(default="change-me-in-production", min_length=16)
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 30
    # Plain comma-separated string (see .env.example), not JSON: pydantic-settings
    # tries to JSON-decode list-typed env values before any field_validator runs,
    # which fails on the documented comma-separated .env/docker-compose form. Kept
    # as a str field and parsed on read instead.
    backend_cors_origins: str = "http://localhost:3000,http://localhost:5173"
    database_url: str = "postgresql+psycopg://grc:grc_password@localhost:5432/grc_platform"
    redis_url: str = "redis://localhost:6379/0"

    ai_provider: str = "echo"
    openai_api_key: str | None = None
    openai_model: str = "gpt-4o-mini"
    azure_openai_endpoint: str | None = None
    azure_openai_api_key: str | None = None
    azure_openai_deployment: str | None = None
    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "llama3"

    @property
    def cors_origins(self) -> list[str]:
        return [origin.strip() for origin in self.backend_cors_origins.split(",") if origin.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
