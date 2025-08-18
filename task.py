from fastapi import APIRouter, Body
from models import StatusType, Task

task_router = APIRouter()
task_list = []

@task_router.get("/")
def get():
    return {"tasks": task_list}

@task_router.post("/")
def add(task: Task):
    # task_list.append({
    #     "task": task,
    #     "status": StatusType.PENDING,
    # })
    # print(task_list)
    
    return {"tasks": task_list}
    
@task_router.put("/")
def update(index: int, task: Task):
    task_list[index] = {
        "task": task.name,
        "status": task.status,
    }
    return {"tasks": task_list}

@task_router.delete("/")
def delete(index: int):
    del task_list[index]
    return {"tasks": task_list}

print("this is a dummy code")
print("This is also dummy")
