import pdfplumber
import os


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


def get_cv_files(directory):
    """
    Retrieves all PDF files from the specified directory.
    """
    return os.path.join(directory, '*.pdf')
