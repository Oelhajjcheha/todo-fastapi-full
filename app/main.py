from fastapi import FastAPI, HTTPException, Depends
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from typing import List
from .database import Base, engine, SessionLocal
from . import schemas, models, crud

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Minimal To-Do API", version="1.0.0")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/health")
def health(): return {"status": "ok"}

@app.get("/api/tasks", response_model=List[schemas.TaskOut])
def list_tasks(db: Session = Depends(get_db)): return crud.get_tasks(db)

@app.post("/api/tasks", response_model=schemas.TaskOut, status_code=201)
def create_task(task_in: schemas.TaskCreate, db: Session = Depends(get_db)): return crud.create_task(db, task_in)

@app.get("/api/tasks/{task_id}", response_model=schemas.TaskOut)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if not task: raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/api/tasks/{task_id}", response_model=schemas.TaskOut)
def update_task(task_id: int, task_update: schemas.TaskUpdate, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if not task: raise HTTPException(status_code=404, detail="Task not found")
    return crud.update_task(db, task, task_update)

@app.delete("/api/tasks/{task_id}", status_code=204)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if not task: raise HTTPException(status_code=404, detail="Task not found")
    crud.delete_task(db, task); return

# Serve minimal frontend
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
