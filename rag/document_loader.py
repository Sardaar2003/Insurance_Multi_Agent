"""
Document Loader
Extracts text from uploaded files.
"""

import tempfile
from pypdf import PdfReader
import docx


def extract_text(uploaded_file):

    file_type = uploaded_file.name.split(".")[-1].lower()

    # save temp file
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        file_path = tmp.name

    # PDF
    if file_type == "pdf":
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text

    # DOCX
    if file_type == "docx":
        doc = docx.Document(file_path)
        return "\n".join([p.text for p in doc.paragraphs])

    # TXT
    if file_type == "txt":
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    return None