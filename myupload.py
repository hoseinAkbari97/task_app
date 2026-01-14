from fastapi import APIRouter, File

upload_router = APIRouter()
@upload_router.post("/file/")
def upload_file(file: bytes = File()):
    return {"file_size": len(file)}
