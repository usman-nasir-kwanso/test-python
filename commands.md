# Project Commands Playbook

Practical command reference for running, testing, and troubleshooting this project.

## Environment Setup

```bash
source venv/bin/activate
python -V
pip install -r requirements.txt
python -m pip check
```

## FastAPI Apps

```bash
# Ollama API
fastapi dev ollama-fastapi/server.py

# RAG Queue API
fastapi dev rag-queue/main.py

# Alternative (uvicorn directly)
uvicorn rag-queue.server:app --reload --port 8080
```

## API Smoke Tests

```bash
# Ollama endpoint
curl -X POST http://127.0.0.1:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"hello"}'

# RAG queue endpoint
curl -X POST "http://127.0.0.1:8080/chat?query=short%20summary"
```

## Queue and Worker (RQ + Valkey)

```bash
# Start queue backend
cd rag-queue && docker compose up -d

# Start worker (new terminal)
cd rag-queue
source ../venv/bin/activate
rq worker

# Check Redis/Valkey connectivity
redis-cli -p 6379 ping
```

## RAG Commands

```bash
# Start Qdrant
cd rag && docker compose up -d

# Build vector index
python rag/index.py

# Ask questions
python rag/chat.py

# Verify Qdrant
curl http://localhost:6333/collections
```

## Prompting Commands

```bash
python prompting/main.py
python prompting/few-shot-prompting.py
python prompting/chain-of-thought.py
python prompting/persona-prompting.py
```

## Prompt Style Commands

```bash
python prompt-styles/chatml-style.py
python prompt-styles/alpaca-style.py
python prompt-styles/llama2-inst-style.py
```

## Other Learning Modules

```bash
python tokenization/main.py
python weather_agent/main.py
python hf-basic/main.py
```

## Quality and Troubleshooting

```bash
# Syntax sanity check
python -m compileall .

# Current git changes
git status

# Find unfinished notes
rg "TODO|FIXME" .

# Verify key local ports in code/config
rg "localhost:8000|localhost:6379|localhost:6333" .

# Running containers
docker ps
```

## Common Fixes

- `ModuleNotFoundError`: activate virtual env first (`source venv/bin/activate`)
- FastAPI CLI missing: `pip install "fastapi[standard]"`
- Queue 500s: ensure Redis/Valkey uses port `6379` in both compose and client config
- RAG empty answers: run indexing first (`python rag/index.py`)

## Docker and Service Logs

```bash
# Show compose services status (from a folder containing docker-compose.yml)
docker compose ps

# Follow logs for a specific service
docker compose logs -f valkey
docker compose logs -f vector-db

# Restart a single service
docker compose restart valkey

# Stop/remove compose stack
docker compose down
```

## Redis/Valkey Queue Inspection

```bash
# Redis ping
redis-cli -p 6379 ping

# Queue length (default queue)
redis-cli -p 6379 llen rq:queue:default

# List all keys (dev-only, avoid in prod)
redis-cli -p 6379 keys '*'
```

## FastAPI Debug Commands

```bash
# Check OpenAPI schema quickly
curl http://127.0.0.1:8000/openapi.json | python -m json.tool | head -n 40

# Health-style check
curl -i http://127.0.0.1:8000/docs

# Verbose request debugging
curl -v -X POST "http://127.0.0.1:8080/chat?query=test"
```

## Python Environment Diagnostics

```bash
# Which Python/pip are active
which python
which pip

# Installed package versions (key libs)
python -c "import fastapi, sqlalchemy, openai; print(fastapi.__version__, sqlalchemy.__version__, openai.__version__)"

# Export exact environment snapshot
pip freeze > requirements.lock.txt
```

## Lint and Type Checks

```bash
# If pylint is available
pylint rag-queue/server.py rag-queue/queues/worker.py

# If pyright/basedpyright is available
pyright .

# Compile all Python files
python -m compileall .
```

## Data and RAG Utilities

```bash
# Count PDF pages quickly (requires pypdf)
python - <<'PY'
from pypdf import PdfReader
r = PdfReader("rag/Djermaya Solar PIM version 01 Final (2019-01-31) - Project Information Memorandum Sample for AI Team.pdf")
print(len(r.pages))
PY

# Quick check Qdrant health
curl -s http://localhost:6333/ | python -m json.tool
```

## Suggested Terminal Workflow

```bash
# Terminal 1: FastAPI (rag-queue)
source venv/bin/activate
python rag-queue/main.py

# Terminal 2: Worker
cd rag-queue
source ../venv/bin/activate
rq worker

# Terminal 3: Queue backend + vector DB
cd rag-queue && docker compose up -d
cd ../rag && docker compose up -d
```
