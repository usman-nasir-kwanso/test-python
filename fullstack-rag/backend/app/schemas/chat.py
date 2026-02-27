"""Schemas used by chat/retrieval endpoints."""

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """Input payload for document-grounded chat."""

    question: str = Field(min_length=1, max_length=2000)
    document_id: str | None = None
    top_k: int = Field(default=5, ge=1, le=20)


class Citation(BaseModel):
    """Citation metadata for retrieved chunks."""

    document_id: str
    filename: str | None = None
    chunk_index: int
    source: str | None = None
    page: int | None = None
    score: float
    snippet: str


class ChatResponse(BaseModel):
    """Grounded answer with retrieval metadata."""

    answer: str
    citations: list[Citation]
    retrieved_chunks_count: int
