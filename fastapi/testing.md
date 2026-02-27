# Testing FastAPI APIs

## Test Layers

1. Unit tests: business logic
2. Integration tests: DB + services
3. API tests: HTTP contracts and status codes

## Basic API Test

```python
from fastapi.testclient import TestClient
from server import app

client = TestClient(app)

def test_health():
    r = client.get('/health')
    assert r.status_code == 200
    assert r.json()['status'] == 'ok'
```

## What to Test for Each Endpoint

- Success path (`200/201`)
- Validation errors (`422`)
- Not-found path (`404`)
- Unauthorized/forbidden (`401/403`)
- Edge cases (empty input, min/max limits)

## Database Testing Tips

- Use separate test DB
- Rollback transaction per test
- Seed minimal deterministic fixtures

## Contract Stability

Validate response shape with Pydantic models or schema assertions.
If schema changes, tests should fail immediately.
