# Advanced FastAPI Topics

## Lifespan Events

Use lifespan for startup/shutdown resources (DB init, model warmup).

```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app):
    # startup
    yield
    # shutdown
```

## Middleware

Common middleware types:

- Request ID/correlation ID
- Logging and metrics
- CORS
- Security headers

## Background Tasks

Use `BackgroundTasks` for short non-critical post-response work.
For long jobs, use queue systems (RQ, Celery, Dramatiq).

## Security Basics

- Prefer OAuth2/JWT for APIs
- Never trust client input
- Validate and sanitize payloads
- Store secrets in env vars, not source code

## Performance Patterns

- Add DB indexes for common filters
- Use pagination for list endpoints
- Avoid N+1 queries
- Keep response payloads small
- Add caching for read-heavy endpoints

## API Versioning

Recommended pattern:

- `/api/v1/...`
- Introduce `/api/v2/...` for breaking changes

## Observability

- Structured logging (JSON in production)
- Request latency metrics
- Error rate alerts
- Health endpoints (`/health`, `/ready`)
