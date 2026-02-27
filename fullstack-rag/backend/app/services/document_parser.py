"""Document parsing for supported file types."""

from io import BytesIO

from fastapi import HTTPException, UploadFile, status
from pypdf import PdfReader


def parse_upload(file: UploadFile, content: bytes) -> str:
    """Extract plain text from uploaded PDF or TXT file."""
    if file.content_type == "application/pdf":
        reader = PdfReader(BytesIO(content))
        text = "\n".join(page.extract_text() or "" for page in reader.pages)
        return text.strip()

    if file.content_type in {"text/plain", "application/octet-stream"}:
        try:
            return content.decode("utf-8").strip()
        except UnicodeDecodeError:
            return content.decode("latin-1").strip()

    raise HTTPException(
        status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
        detail="Only PDF and TXT files are supported",
    )
