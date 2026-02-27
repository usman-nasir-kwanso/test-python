"""Application settings loaded from environment variables."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Typed runtime configuration."""

    app_name: str = "Fullstack RAG API"
    environment: str = "development"
    openai_api_key: str
    openai_embedding_model: str = "text-embedding-3-small"
    openai_chat_model: str = "gpt-4o-mini"
    qdrant_url: str = "http://localhost:6333"
    qdrant_collection: str = "documents"
    max_upload_bytes: int = 10 * 1024 * 1024  # 10 MB
    chunk_size: int = 900
    chunk_overlap: int = 150
    top_k_default: int = 5

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
