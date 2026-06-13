from pypdf import PdfReader

def read_pdf(pdf):
    text = ""

    reader = PdfReader(pdf)

    for page in reader.pages:
        text += page.extract_text()

    return text