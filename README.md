# Minimal To-Do Application (FastAPI + SQLite)

A clean CRUD To-Do app built using **FastAPI**, **SQLite**, and a minimal **HTML frontend**.  
Designed to demonstrate full SDLC documentation and DevOps readiness (Docker + CI/CD).

## 🚀 Features
- Create, Read, Update, Delete tasks (CRUD)
- Persistent SQLite database
- REST API endpoints via FastAPI
- Auto-generated Swagger docs
- Minimal, functional frontend
- Dockerfile and CI pipeline (GitHub Actions)

## 🧠 Tech Stack
| Component | Technology |
|------------|-------------|
| Backend | FastAPI (Python 3.11) |
| Database | SQLite (SQLAlchemy ORM) |
| Frontend | HTML + Vanilla JavaScript |
| DevOps | Docker, GitHub Actions |

## ⚙️ Setup
```bash
# Clone repo
git clone <your_repo_url>
cd todo-fastapi

# Create venv
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn app.main:app --reload
```

- Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) for UI  
- Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for API docs

## 🐳 Docker Usage
```bash
docker build -t todo-fastapi .
docker run -p 8000:8000 todo-fastapi
```

## ✅ API Overview
| Method | Endpoint | Description |
|--------|-----------|-------------|
| GET | /api/tasks | Retrieve all tasks |
| POST | /api/tasks | Create a new task |
| PUT | /api/tasks/{id} | Update a task |
| DELETE | /api/tasks/{id} | Delete a task |
| GET | /api/health | Health check |

## 📂 Structure
```
todo-fastapi/
├── app/
├── frontend/
├── docs/
├── .github/
├── Dockerfile
├── requirements.txt
└── README.md
```

## 🧾 Version Control
- **Commit 1:** Add CRUD backend and frontend
- **Commit 2:** Add SDLC report and diagrams
- **Commit 3:** Add Dockerfile and CI workflow

## 🧠 DevOps Reflection
This app can be integrated into a DevOps pipeline with CI/CD, Docker deployment, and cloud scalability.  
Future enhancements include automated testing, multi-environment support, and continuous deployment.
