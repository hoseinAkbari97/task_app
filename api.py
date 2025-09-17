from fastapi import FastAPI, APIRouter, Query, Path

from task import task_router

app = FastAPI()
router = APIRouter()

@router.get('/hello')
def hello_world():
    return { "hello": "world" }


@app.get("/e_page")
def page(page: int = Query(1, ge=1, le=20, title='page'),
          size: int = Query(5, ge=5, le=20, title='page size')):
    return { "page": page,"size": size }

@app.get("/e_phone/") # +34 111 12-34-56
def phone1(phone: str = Query(regex=r"^(\(?\+[\d]{1,3}\)?)\s?([\d]{1,5})\s?([\d][\s\.-]?){6,7}$", example="+34 111 12-34-56")):
    return {"phone": phone}

@app.get("/ep_phone/{phone}")
def phone(phone: str =
    Path(
        pattern=r"^(\(?\+[\d]{1,3}\)?)\s?([\d]{1,5})\s?([\d][\s\.-]?){6,7}$",
        examples=[
            {
                "summary": "A normal example 1",
                "description": "A normal example",
                "value": "+34 111 12-34-56"
            },
            {
                "summary": "A normal example 2",
                "description": "A normal example",
                "value": "+34 111 12-34-59"
            }
        ]
    )
):
    return {"phone": phone}
    return {"phone": phone}


app.include_router(router)
app.include_router(task_router, prefix='/tasks')
