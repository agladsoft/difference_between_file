from docx import Document
from io import StringIO, BytesIO


def get_docs(txt):
    document = Document()
    for paragraph in txt.decode("utf-8").split('\n'):
        document.add_paragraph(paragraph)
    document.save('test.docx')
    return document

