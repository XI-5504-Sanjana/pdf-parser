import pytesseract
from pdf2image import convert_from_path

POPPLER_PATH = r"C:\Users\Sanjana Nayak\Downloads\Release-25.12.0-0\poppler-25.12.0\Library\bin"

def extract_ocr(pdf_path):

    ocr_text = ""

    images = convert_from_path(
        pdf_path,
        poppler_path=POPPLER_PATH
    )

    for i, image in enumerate(images):

        text = pytesseract.image_to_string(image)

        ocr_text += f"\n--- OCR Page {i+1} ---\n"
        ocr_text += text

    return ocr_text