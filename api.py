from fastapi import FastAPI, APIRouter
from task import task_router

app = FastAPI()
router = APIRouter()

@router.get("/hello")
def hello_world() -> dict:
    return {"hello": "world"}

@router.get("/posts/{id}")
def add(id: int) -> dict:
    return {"post_id": id}


app.include_router(router)
app.include_router(task_router, prefix="/tasks")
