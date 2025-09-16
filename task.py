from fastapi import APIRouter, Body, status, HTTPException
from models import Task

task_router = APIRouter()
task_list = []

@task_router.get("/{index}", status_code=status.HTTP_200_OK)
def get(index: int):

    if len(task_list) <= index:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task ID Doesn't Exist!!",
        )
    return {"tasks": task_list[index]}

@task_router.post("/", status_code=status.HTTP_201_CREATED)
def add(task: Task):
    if task in task_list:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Task " + task.name + " already exists!"
        )
    task_list.append(task)
    return {"tasks": status.HTTP_201_CREATED}
    
@task_router.put("/", status_code=status.HTTP_200_OK)
def update(index: int, task: Task = Body(
    example= {
        "id": 123,
        "name": "xavier",
    }
)):
    if len(task_list) <= index:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task ID Doesn't exist!!",
        )
    
    task_list[index] = {
        "task": task.name,
        "status": task.status,
    }
    return {"tasks": task_list}

@task_router.delete("/", status_code=status.HTTP_200_OK)
def delete(index: int):
    del task_list[index]
    return {"tasks": task_list}
