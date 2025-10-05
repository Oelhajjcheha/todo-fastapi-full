# Minimal To-Do Application (FastAPI + SQLite)

A clean CRUD To-Do app built using **FastAPI**, **SQLite**, and a minimal **HTML frontend**.
Designed to demonstrate full SDLC documentation and DevOps readiness (Docker + CI/CD).

## Quickstart
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```
- UI: http://127.0.0.1:8000/
- API docs: http://127.0.0.1:8000/docs

## Docker
```bash
docker build -t todo-fastapi .
docker run -p 8000:8000 todo-fastapi
```

## Structure
```
app/          # FastAPI app (CRUD + DB)
frontend/     # Minimal UI
docs/         # Diagrams + report
.github/      # CI workflow
Dockerfile
requirements.txt
README.md
```
