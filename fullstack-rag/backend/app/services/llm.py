"""LLM response generation service."""

from openai import OpenAI

from app.core.config import settings

_openai_client = OpenAI(api_key=settings.openai_api_key)


def generate_answer(question: str, context: str) -> str:
    """Generate a grounded answer using retrieved context."""
    system_prompt = (
        "You are a document QA assistant. "
        "Answer only from the provided context. "
        "If context is insufficient, say you don't have enough information."
    )
    user_prompt = f"Question:\n{question}\n\nContext:\n{context}"

    response = _openai_client.chat.completions.create(
        model=settings.openai_chat_model,
        temperature=0.2,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    return response.choices[0].message.content or "No answer generated."
