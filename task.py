from fastapi import APIRouter

task_router = APIRouter()
task_list = []

@task_router.get("/")
def get():
    return {"tasks": task_list}
