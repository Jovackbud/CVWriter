import glob
import os
import pdfplumber


def get_file(directory):
    """
    Retrieves the single PDF file from the specified JD directory.
    Throws an error if there are zero or more than one PDF file.
    """
    cv = glob.glob(os.path.join(directory, '*.pdf'))
    if len(cv) != 1:
        raise ValueError(f"Expected exactly one PDF file in {directory}, but found {len(cv)}.")
    return cv[0]


def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file.
    """
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ''.join(page.extract_text() for page in pdf.pages if page.extract_text())
        return text
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {e}")
        return ""


