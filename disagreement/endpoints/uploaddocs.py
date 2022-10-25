from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from disagreement.schemas.input_data import InputData
from disagreement.utils import save_disagreement


router = APIRouter()


@router.post("/get_disagreement/")
async def get_disagreement(input_data: InputData):
    file = save_disagreement(input_data.docx, input_data.pdf, input_data.countError)
    return StreamingResponse(file, media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
