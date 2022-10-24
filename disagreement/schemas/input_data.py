from fastapi import FastAPI
from pydantic import BaseModel


class InputData(BaseModel):
    docx: str
    pdf: str
    countError: int = 0
