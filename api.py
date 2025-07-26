from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def hello_world() -> dict:
    return {"hello": "world"}

@app.get("/posts/{id}")
def add(id: int) -> dict:
    # TODO
    return {"post_id": id}
