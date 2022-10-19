from io import BytesIO
from typing import List

from fastapi import APIRouter, File, UploadFile

from disagreement.utils.difference import save_disagreement

router = APIRouter()


@router.post("/uploaddocs/")
async def create_upload_files(
    files: List[UploadFile] = File(description="Multiple files as UploadFile"),
):
    file1, file2 = files
    save_disagreement(BytesIO(file1.file.read()), BytesIO(file2.file.read()))
    return {"filenames": [file.filename for file in files]}
