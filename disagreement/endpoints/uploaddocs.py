from io import BytesIO

from docx import Document
from fastapi import APIRouter, File, UploadFile

from disagreement.utils import save_disagreement
from disagreement.utils import get_docs

router = APIRouter()


@router.post("/uploaddocs/")
async def create_upload_files(
    txt: UploadFile = File,
    docx: UploadFile = File,
):
    save_disagreement(Document((BytesIO(docx.file.read()))), get_docs(txt.file.read()))
    return {"message": "Disagreements created"}
