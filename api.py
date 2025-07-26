from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def hello_world() -> dict:
    return {"hello": "world"}