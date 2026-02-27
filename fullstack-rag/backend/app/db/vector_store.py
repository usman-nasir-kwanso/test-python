"""Qdrant vector store utilities."""

import uuid

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, FieldCondition, Filter, MatchValue, PointStruct, VectorParams

from app.core.config import settings

VECTOR_SIZE = 1536  # text-embedding-3-small

_qdrant = QdrantClient(url=settings.qdrant_url)


def ensure_collection() -> None:
    """Create collection if it does not exist."""
    existing = _qdrant.get_collections().collections
    names = {collection.name for collection in existing}
    if settings.qdrant_collection not in names:
        _qdrant.create_collection(
            collection_name=settings.qdrant_collection,
            vectors_config=VectorParams(size=VECTOR_SIZE, distance=Distance.COSINE),
        )


def upsert_document_chunks(
    document_id: str,
    filename: str,
    chunks: list[str],
    embeddings: list[list[float]],
) -> None:
    """Upsert chunk vectors and metadata into Qdrant."""
    points: list[PointStruct] = []
    for idx, (chunk, embedding) in enumerate(zip(chunks, embeddings, strict=True)):
        points.append(
            PointStruct(
                id=str(uuid.uuid4()),
                vector=embedding,
                payload={
                    "document_id": document_id,
                    "filename": filename,
                    "chunk_index": idx,
                    "source": filename,
                    "text": chunk,
                },
            )
        )

    _qdrant.upsert(collection_name=settings.qdrant_collection, points=points)


def similarity_search(
    query_vector: list[float], top_k: int, document_id: str | None = None
):
    """Search top-k nearest chunks, optionally filtered by document_id."""
    query_filter = None
    if document_id:
        query_filter = Filter(
            must=[
                FieldCondition(
                    key="document_id",
                    match=MatchValue(value=document_id),
                )
            ]
        )
    return _qdrant.search(
        collection_name=settings.qdrant_collection,
        query_vector=query_vector,
        limit=top_k,
        query_filter=query_filter,
    )
