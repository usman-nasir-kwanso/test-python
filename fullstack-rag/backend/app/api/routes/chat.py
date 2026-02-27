"""Document-grounded chat endpoints."""

from fastapi import APIRouter, HTTPException, status

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.embeddings import embed_query
from app.services.llm import generate_answer
from app.services.retrieval import build_context_and_citations
from app.db.vector_store import similarity_search

router = APIRouter(prefix="/api", tags=["chat"])


@router.post("/chat", response_model=ChatResponse)
async def chat_with_document(payload: ChatRequest) -> ChatResponse:
    """Answer question using retrieval from embedded document chunks."""
    query_vec = embed_query(payload.question)
    results = similarity_search(
        query_vector=query_vec,
        top_k=payload.top_k,
        document_id=payload.document_id,
    )
    if not results:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No relevant chunks found. Upload document first or change query.",
        )

    context, citations = build_context_and_citations(results)
    answer = generate_answer(payload.question, context)

    return ChatResponse(
        answer=answer,
        citations=citations,
        retrieved_chunks_count=len(citations),
    )
