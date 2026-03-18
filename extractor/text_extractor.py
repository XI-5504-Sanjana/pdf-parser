#handles normal pdf text extraction uses PyMUpdf
#pdf to extract machine readacle text 
import fitz  # PyMuPDF


def extract_text(pdf_path):

    text_data = ""

    doc = fitz.open(pdf_path)

    for page_num in range(len(doc)):

        page = doc.load_page(page_num)
        text = page.get_text()

        text_data += f"\n--- Page {page_num+1} Text ---\n"
        text_data += text

    return text_data