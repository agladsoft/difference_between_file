from docx import Document


def get_docs(txt: bytes) -> Document:
    document = Document()
    for paragraph in txt.decode("utf-8").split("\n"):
        document.add_paragraph(paragraph)
    return document
