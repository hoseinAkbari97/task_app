from fastapi import APIRouter, File, UploadFile
import shutil

upload_router = APIRouter()

@upload_router.post("/file/")
def upload_file(file: bytes = File()):
    return {"file_size": len(file)}

@upload_router.post("/uploadfile1/")
def upload_file1(file: UploadFile):
    return {
        "filename": file.filename, 
        "content_type": file.content_type,
        }
    
@upload_router.post("/uploadfile2/")
def upload_file2(file: UploadFile):
    
    with open(f"img/uploaded_{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}
