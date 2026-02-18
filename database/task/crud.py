from sqlalchemy.orm import Session

from schemas import Task
from database import models

def getById(db: Session, id: int):
    # task = db.query(models.Task).filter(models.Task.id == id).first()
    task = db.query(models.Task).get(id)
    return task

def getAll(db: Session):
    tasks = db.query(models.Task).all()
    return tasks

def create(task: Task, db: Session):
    taskdb = models.Task(name=task.name, description=task.description, status=task.status)
    db.add(taskdb)
    db.commit()
    db.refresh(taskdb)
    return taskdb

def update(id: int, task: Task, db: Session):
    
    taskdb = getById(id, db)
    
    taskdb.name = task.name
    taskdb.description = task.description
    taskdb.status = task.status
    
    db.add(taskdb)
    db.commit()
    db.refresh(taskdb)
    return taskdb

def delete(task: Task, db: Session):
    db.delete(task)
    db.commit()
    