# Deployment Runbook

## Production App Server

Use Gunicorn + Uvicorn workers:

```bash
gunicorn server:app -k uvicorn.workers.UvicornWorker -w 2 -b 0.0.0.0:8000
```

## Environment Configuration

Required:

- `OPENAI_API_KEY` and other secrets in env
- `ENV=production`
- DB URL and queue URLs

## Reverse Proxy

Place FastAPI behind Nginx/Traefik for:

- TLS termination
- Rate limiting
- Request buffering/timeouts

## Deployment Checklist

- [ ] Health endpoints available
- [ ] Migrations applied
- [ ] Logs/metrics configured
- [ ] CORS configured correctly
- [ ] Timeouts/retries configured for external calls
- [ ] Security headers enabled
- [ ] Alerting configured

## Failure Handling

- Use graceful shutdown signals
- Set timeouts for all outbound HTTP calls
- Add retry with backoff for transient failures
- Keep endpoints idempotent where possible

## Post-Deploy Verification

1. Check `/docs` and `/health`
2. Smoke test critical endpoints
3. Verify logs for startup/runtime errors
4. Confirm baseline latency and error rate
