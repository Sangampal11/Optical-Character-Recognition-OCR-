from PIL import Image
import pytesseract
import fitz  # PyMuPDF
import re
import json

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    """Extract text from a JPEG image using OCR."""
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file using OCR."""
    text = ""
    pdf_document = fitz.open(pdf_path)
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        pix = page.get_pixmap()
        image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        text += pytesseract.image_to_string(image)
    return text

def extract_text(file_path):
    """Extract text from a file (JPEG or PDF)."""
    if file_path.lower().endswith('.jpeg') or file_path.lower().endswith('.jpg'):
        return extract_text_from_image(file_path)
    elif file_path.lower().endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    else:
        raise ValueError("Unsupported file format. Please provide a JPEG or PDF file.")