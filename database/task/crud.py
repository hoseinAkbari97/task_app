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

