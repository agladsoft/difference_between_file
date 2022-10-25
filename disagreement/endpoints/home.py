from fastapi import APIRouter
from fastapi.responses import HTMLResponse


router = APIRouter()


@router.get("/")
async def main():
    content = """
        <body>
        <form action="/uploaddocs/" enctype="multipart/form-data" method="post">
        <p>*.txt: <input name="txt" type="file"></p>
        <p>*.docx: <input name="docx" type="file"></p>
        <p>Допустимое кол-во ошибок в абзаце <input name="count_errors" type="text" value="0"></p>
        <br>
        <input type="submit">
        </form>
        </body>
        """
    return HTMLResponse(content=content)
