"""FastAPI server that queues RAG queries."""

from fastapi import FastAPI, Query
from client.rq_client import queue
from queues.worker import process_query

app = FastAPI()


@app.post("/chat")
async def chat(query: str = Query(..., description="The question to ask")):
    """Queue a RAG query and return the answer."""
    job = queue.enqueue(process_query, query)
    return {"job_id": job.id, "status": "queued"}
