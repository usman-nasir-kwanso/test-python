"""FastAPI server that chats with a local Ollama model."""

from fastapi import Body, FastAPI
from ollama import ChatResponse, Client

app = FastAPI()
client = Client(
    host="http://localhost:11434",
)

MODEL = "gemma:2b"


@app.post("/chat")
async def chat(message: str = Body(..., description="The message to chat with Ollama")):
    """Send a message to Ollama and return the reply."""
    response: ChatResponse = client.chat(
        model=MODEL,
        messages=[{"role": "user", "content": message}],
        stream=False,
    )

    return {"response": response.message.content}
