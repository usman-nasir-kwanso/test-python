# Ollama + FastAPI

A simple REST API that wraps a local Ollama model behind a FastAPI endpoint.

## How It Works

```
Client  -->  POST /chat  -->  FastAPI  -->  Ollama (local)  -->  Response
```

1. Client sends a message via `POST /chat`
2. FastAPI forwards it to Ollama running on `localhost:11434`
3. Ollama generates a response using the `gemma:2b` model
4. FastAPI returns the reply as JSON

## Prerequisites

- [Ollama](https://ollama.com/) installed and running locally
- A model pulled: `ollama pull gemma:2b`

## Run

```bash
source venv/bin/activate
fastapi dev ollama-fastapi/server.py
```

Server starts at `http://127.0.0.1:8000`

## API

### POST /chat

**Request:**
```json
{"message": "What is Python?"}
```

**Response:**
```json
{"response": "Python is a high-level programming language..."}
```

**Test with curl:**
```bash
curl -X POST http://127.0.0.1:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "hello"}'
```

**Docs:** `http://127.0.0.1:8000/docs` (auto-generated Swagger UI)

## Troubleshooting

- **`ModuleNotFoundError: fastapi`**: activate venv and install extras: `pip install "fastapi[standard]"`.
- **`Connection refused` to Ollama**: start Ollama and verify `http://localhost:11434` is reachable.
- **Model not found**: run `ollama pull gemma:2b` before requests.
- **422 validation errors**: ensure request body is JSON and contains `message`.
- **Slow responses**: first request may be slow due to model warmup; subsequent calls are faster.

## Related Docs

- [`../fastapi/README.md`](../fastapi/README.md) for FastAPI concepts and production patterns
