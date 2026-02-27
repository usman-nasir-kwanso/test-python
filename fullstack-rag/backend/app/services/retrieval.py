"""Retrieval helpers to convert search results into context/citations."""

from app.schemas.chat import Citation


def build_context_and_citations(results) -> tuple[str, list[Citation]]:
    """Build context text and citation payload from Qdrant search results."""
    context_blocks: list[str] = []
    citations: list[Citation] = []

    for item in results:
        payload = item.payload or {}
        snippet = str(payload.get("text", ""))[:300]
        context_blocks.append(
            f"[Chunk {payload.get('chunk_index', '?')}] {payload.get('text', '')}"
        )
        citations.append(
            Citation(
                document_id=str(payload.get("document_id", "")),
                filename=str(payload.get("filename")) if payload.get("filename") else None,
                chunk_index=int(payload.get("chunk_index", 0)),
                source=str(payload.get("source")) if payload.get("source") else None,
                page=int(payload.get("page")) if payload.get("page") else None,
                score=float(item.score),
                snippet=snippet,
            )
        )

    return "\n\n".join(context_blocks), citations
