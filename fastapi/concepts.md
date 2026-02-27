# Core Concepts

## 1) Routing

```python
from fastapi import FastAPI

app = FastAPI()

@app.get('/health')
def health() -> dict[str, str]:
    return {'status': 'ok'}
```

## 2) Request Data Sources

- Path params: `/users/{user_id}`
- Query params: `?limit=20`
- Body params: JSON payload for create/update

## 3) Validation with Pydantic

```python
from pydantic import BaseModel, Field

class CreateUser(BaseModel):
    email: str
    age: int = Field(ge=13)
```

FastAPI automatically validates and returns `422` for invalid payloads.

## 4) Response Models

Use `response_model=` to enforce API output contracts.

```python
@app.post('/users', response_model=UserOut)
def create_user(payload: CreateUser):
    ...
```

## 5) Dependency Injection

Common for DB sessions, auth, config, and shared services.

```python
from fastapi import Depends

@app.get('/items')
def list_items(db = Depends(get_db)):
    ...
```

## 6) Error Handling

- Raise `HTTPException` for business errors
- Add global handlers for consistent response format

```python
from fastapi import HTTPException
raise HTTPException(status_code=404, detail='Item not found')
```

## 7) Status Codes

- `200` read success
- `201` created
- `400` bad request
- `401/403` auth/permission
- `404` missing resource
- `422` validation error
- `500` server error

## 8) Async vs Sync

- Use `async def` for I/O-bound workflows (HTTP calls, async DB drivers)
- Use `def` for CPU-bound/simple sync operations
- Do not block event loop with heavy CPU operations
