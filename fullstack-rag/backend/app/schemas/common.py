"""Shared API schema models."""

from pydantic import BaseModel


class ErrorResponse(BaseModel):
    """Standardized API error payload."""

    error: str
    details: str
