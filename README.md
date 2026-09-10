# Python Docker Service

A minimal Python HTTP service packaged with Docker. It provides a small, reproducible example of containerizing an application with an explicit health check and a non-root runtime user.

## Endpoints

| Endpoint | Response |
| --- | --- |
| `GET /` | Service name and status |
| `GET /health` | Health status for container orchestration |

## Run with Docker Compose

```bash
docker compose up --build
```

The service is available at `http://localhost:8000`.

```bash
curl http://localhost:8000/
curl http://localhost:8000/health
```

To use another host port:

```bash
PORT=8080 docker compose up --build
```

## Run without Docker

```bash
PORT=8000 python app/app.py
```

## Container design

- Python 3.11 slim base image
- Runs as a dedicated non-root user
- Exposes port `8000`
- Uses Docker `HEALTHCHECK` against `/health`
- Excludes local and Git metadata through `.dockerignore`
