from sqlalchemy.orm import Session
from . import models, schemas

def get_tasks(db: Session):
    return db.query(models.Task).order_by(models.Task.id).all()

def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def create_task(db: Session, task_in: schemas.TaskCreate):
    task = models.Task(title=task_in.title, completed=task_in.completed)
    db.add(task); db.commit(); db.refresh(task)
    return task

def update_task(db: Session, task, task_update: schemas.TaskUpdate):
    if task_update.title is not None:
        task.title = task_update.title
    if task_update.completed is not None:
        task.completed = task_update.completed
    db.commit(); db.refresh(task)
    return task

def delete_task(db: Session, task):
    db.delete(task); db.commit()
