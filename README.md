# Python AI/LLM Learning Project

A hands-on collection of Python scripts exploring AI/LLM fundamentals — from tokenization to prompting techniques to local model serving.

## Project Structure

```
python-v2/
├── tokenization/       # How LLMs break text into tokens
├── prompting/          # Prompting techniques (few-shot, CoT, persona)
├── prompt-styles/      # Prompt format comparison (ChatML, Alpaca, LLaMA-2)
├── ollama-fastapi/     # REST API wrapping a local Ollama model
├── hf-basic/           # Hugging Face transformers pipeline
├── weather_agent/      # AI agent with function calling (real weather data)
├── rag/                # RAG — ask questions about a PDF
├── rag-queue/          # Queue-based RAG pipeline with FastAPI + RQ + Valkey
├── cursor-pagination/  # Cursor-based pagination reference docs
├── fastapi/            # FastAPI concept handbook and production guides
├── requirements.txt
└── venv/
```

## Quick Start

```bash
# Activate the virtual environment
source venv/bin/activate

# Run any script
python tokenization/main.py
python prompting/few-shot-prompting.py
python prompt-styles/chatml-style.py
```

## Topics Covered

| Folder | What You'll Learn |
|---|---|
| `tokenization/` | How text becomes tokens, encoding/decoding with tiktoken |
| `prompting/` | Basic, few-shot, chain-of-thought, and persona prompting |
| `prompt-styles/` | ChatML vs Alpaca vs LLaMA-2 [INST] formatting |
| `ollama-fastapi/` | Serving a local LLM behind a REST API |
| `hf-basic/` | Using Hugging Face pipelines for multimodal inference |
| `weather_agent/` | Function calling — model decides when to call your code |
| `rag/` | Retrieval-Augmented Generation — Q&A over PDFs with vector search |
| `rag-queue/` | Async RAG processing using queue workers |
| `cursor-pagination/` | Scalable pagination strategy for APIs |
| `fastapi/` | Core-to-advanced FastAPI concepts and production runbooks |

## Requirements

- Python 3.12+
- OpenAI API key (for prompting scripts) — set in `.env`
- Ollama (for ollama-fastapi) — [install here](https://ollama.com/)
- Docker (for rag) — runs Qdrant vector database

## Documentation Index

- [`tokenization/README.md`](tokenization/README.md)
- [`prompting/README.md`](prompting/README.md)
- [`prompt-styles/README.md`](prompt-styles/README.md)
- [`ollama-fastapi/README.md`](ollama-fastapi/README.md)
- [`hf-basic/README.md`](hf-basic/README.md)
- [`weather_agent/README.md`](weather_agent/README.md)
- [`rag/README.md`](rag/README.md)
- [`rag-queue/README.md`](rag-queue/README.md)
- [`cursor-pagination/README.md`](cursor-pagination/README.md)
- [`fastapi/README.md`](fastapi/README.md)

## Where to Start (Beginner Path)

1. Start with [`tokenization/README.md`](tokenization/README.md)
2. Move to [`prompting/README.md`](prompting/README.md)
3. Compare formats in [`prompt-styles/README.md`](prompt-styles/README.md)
4. Learn function tools in [`weather_agent/README.md`](weather_agent/README.md)
5. Build retrieval systems via [`rag/README.md`](rag/README.md) and [`rag-queue/README.md`](rag-queue/README.md)
6. Study framework best practices in [`fastapi/README.md`](fastapi/README.md)
