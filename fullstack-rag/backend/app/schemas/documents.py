"""Schemas used by document upload/indexing endpoints."""

from pydantic import BaseModel


class UploadResponse(BaseModel):
    """Result returned after indexing an uploaded document."""

    document_id: str
    filename: str
    chunks_indexed: int
    status: str
