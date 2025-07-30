from fastapi import FastAPI, APIRouter

app = FastAPI()
# @app.get("/")
# def hello_world() -> dict:
#     return {"hello": "world"}
router = APIRouter()
@router.get("/")
def hello_world() -> dict:
    return {"hello": "world"}

@router.get("/posts/{id}")
def add(id: int) -> dict:
    return {"post_id": id}

app.include_router(router)

# @app.get("/posts/{id}")
# def add(id: int) -> dict:
#     # TODO
#     return {"post_id": id}
