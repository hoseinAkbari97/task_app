from fastapi import APIRouter

task_router = APIRouter()
task_list = []

@task_router.get("/")
def get():
    return {"tasks": task_list}

@task_router.post("/{task}")
def add(task: str):
    task_list.append(task)
    return {"tasks": task_list}
    
@task_router.put("/")
def update(index: int, task: str):
    task_list[index] = task
    return {"tasks": task_list}

@task_router.delete("/")
def delete(index: int):
    del task_list[index]
    return {"tasks": task_list}
