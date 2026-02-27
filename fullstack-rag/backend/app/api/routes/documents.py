"""Document upload and indexing endpoints."""

import uuid

from fastapi import APIRouter, File, HTTPException, UploadFile, status

from app.core.config import settings
from app.db.vector_store import ensure_collection, upsert_document_chunks
from app.schemas.documents import UploadResponse
from app.services.chunking import split_text
from app.services.document_parser import parse_upload
from app.services.embeddings import embed_texts

router = APIRouter(prefix="/api/documents", tags=["documents"])


@router.post("/upload", response_model=UploadResponse)
async def upload_document(file: UploadFile = File(...)) -> UploadResponse:
    """Upload a document and index it into Qdrant."""
    raw = await file.read()
    if not raw:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="File is empty")
    if len(raw) > settings.max_upload_bytes:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail=f"File too large. Max size is {settings.max_upload_bytes} bytes",
        )

    text = parse_upload(file, raw)
    if not text:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Could not extract text from file",
        )

    chunks = split_text(text, settings.chunk_size, settings.chunk_overlap)
    if not chunks:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No chunks created")

    embeddings = embed_texts(chunks)
    document_id = str(uuid.uuid4())

    ensure_collection()
    upsert_document_chunks(
        document_id=document_id,
        filename=file.filename or "uploaded_document",
        chunks=chunks,
        embeddings=embeddings,
    )

    return UploadResponse(
        document_id=document_id,
        filename=file.filename or "uploaded_document",
        chunks_indexed=len(chunks),
        status="indexed",
    )
