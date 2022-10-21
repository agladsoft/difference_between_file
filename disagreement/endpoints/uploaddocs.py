from io import BytesIO

from docx import Document
from fastapi import APIRouter, File, UploadFile, Form
from fastapi.responses import StreamingResponse

from disagreement.utils import save_disagreement
from disagreement.utils import get_docs

router = APIRouter()


@router.post("/get_disagreement/", response_class=StreamingResponse)
async def create_upload_files(
    txt: UploadFile = File(),
    docx: UploadFile = File(),
    count_errors: int = Form(),
):
    txt_file = get_docs(txt.file.read())
    docx_file = Document((BytesIO(docx.file.read())))
    file = save_disagreement(docx_file, txt_file, count_errors)

    return StreamingResponse(file, media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
