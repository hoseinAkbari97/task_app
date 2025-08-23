from fastapi import FastAPI, APIRouter, Query, Path
from task import task_router

app = FastAPI()
router = APIRouter()

@router.get("/hello")
def hello_world() -> dict:
    return {"hello": "world"}

@router.get("/posts/{id}")
def add(id: int) -> dict:
    return {"post_id": id}

@app.get("/page/{page}")
def page(
    page: int = Path(gt=0, title='page visualizer'),
    size: int = Query(5, ge=5, le=20)
):
    return {"page": page, "size": size}

@app.get("/phone/{phone}")
# The phone number is like +34 111 12-34-56
def phone(
    phone: str = 
    Path(pattern=r"^(\(?\+[\d]{1,3}\)?)\s?([\d]{1,5})\s?([\d][\s\.-]?){6,7}$" )
):
    return {"phone": phone}

app.include_router(router)
app.include_router(task_router, prefix="/tasks")

# A dummy comment to test git changes
print("This is a dummy print statement to test git changes 2.")
