"""Embedding service wrappers."""

from openai import OpenAI

from app.core.config import settings

_openai_client = OpenAI(api_key=settings.openai_api_key)


def embed_texts(texts: list[str]) -> list[list[float]]:
    """Embed a batch of texts with OpenAI."""
    if not texts:
        return []
    response = _openai_client.embeddings.create(
        model=settings.openai_embedding_model,
        input=texts,
    )
    return [item.embedding for item in response.data]


def embed_query(query: str) -> list[float]:
    """Embed a single query for vector search."""
    return embed_texts([query])[0]
