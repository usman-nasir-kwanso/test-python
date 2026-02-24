# RAG (Retrieval-Augmented Generation)

Ask questions about a PDF and get accurate answers backed by the actual document — not hallucinations.

## What is RAG?

LLMs are smart but they don't know your private data. RAG solves this:

```
         Your Question
              |
              v
  ┌───────────────────────┐
  │  1. Search Vector DB  │  ← Find relevant chunks from your PDF
  │  2. Build Context     │  ← Combine the best matches
  │  3. Ask the LLM       │  ← "Answer based on THIS context"
  └───────────────────────┘
              |
              v
     Accurate Answer + Page Number
```

Instead of asking the LLM to guess, we **retrieve** the relevant information first, then **generate** an answer grounded in that data.

## Files

| File | Purpose |
|---|---|
| `index.py` | **Indexing** — Load PDF, split into chunks, embed, store in Qdrant |
| `chat.py` | **Querying** — Take user question, search vectors, ask LLM with context |
| `docker-compose.yml` | Runs Qdrant vector database locally |

## How It Works (Step by Step)

### Step 1: Indexing (`index.py`)

```
PDF → Load pages → Split into chunks → Embed → Store in Qdrant
```

1. **Load** the PDF using `PyPDFLoader` (extracts text per page)
2. **Split** into 1000-character chunks with 300-character overlap (so no info is lost at boundaries)
3. **Embed** each chunk using OpenAI's `text-embedding-3-small` model (converts text → vector)
4. **Store** vectors in Qdrant (a vector database) with metadata (page number, source file)

### Step 2: Querying (`chat.py`)

```
Question → Embed → Search Qdrant → Build context → Ask GPT → Answer
```

1. **User asks** a question
2. **Similarity search** finds the most relevant chunks from the vector DB
3. **Context is built** with page content + page numbers + file location
4. **GPT answers** using only the retrieved context, pointing to specific pages

## Prerequisites

- OpenAI API key in `.env`
- Docker (for Qdrant)

## Run

```bash
# 1. Start the vector database
docker compose up -d

# 2. Index the PDF (only once)
source venv/bin/activate
python rag/index.py

# 3. Ask questions
python rag/chat.py
```

## Key Concepts

| Concept | What It Means |
|---|---|
| **Embedding** | Converting text into a number array (vector) that captures meaning |
| **Vector DB** | A database optimized for finding similar vectors (Qdrant, Pinecone, etc.) |
| **Similarity Search** | "Find chunks whose meaning is closest to this question" |
| **Chunking** | Breaking a large document into smaller pieces the LLM can digest |
| **Chunk Overlap** | Chunks share some text at boundaries so context isn't cut mid-sentence |
| **Context Window** | The max text an LLM can read at once — RAG keeps it focused |

## Why Not Just Paste the Whole PDF?

- PDFs can be hundreds of pages — won't fit in the context window
- Even if it fits, the LLM gets distracted by irrelevant sections
- RAG retrieves only the **relevant** parts, so answers are focused and accurate
