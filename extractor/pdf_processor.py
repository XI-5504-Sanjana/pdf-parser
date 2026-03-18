
# import fitz
# import camelot

# def process_pdf(pdf_path):

#     doc = fitz.open(pdf_path)
#     combined_text = ""

#     for page_num in range(len(doc)):

#         combined_text += f"\n--- Page {page_num+1} Text ---\n"

#         # Extract text
#         page = doc.load_page(page_num)
#         text = page.get_text()
#         combined_text += text

#         # Extract tables ONLY from this page
#         try:
#             tables = camelot.read_pdf(pdf_path, pages=str(page_num+1))

#             for i, table in enumerate(tables):
#                 combined_text += f"\n--- Table {i+1} (Page {page_num+1}) ---\n"
#                 combined_text += table.df.to_string()

#         except:
#             combined_text += "\n(No tables found on this page)\n"

#     return combined_text


# import fitz
# import camelot

# def process_pdf(pdf_path):

#     doc = fitz.open(pdf_path)
#     combined_text = ""

#     for page_num in range(len(doc)):

#         combined_text += f"\n--- Page {page_num+1} Text ---\n"

#         page = doc.load_page(page_num)

#         # Extract tables first
#         tables = []
#         try:
#             tables = camelot.read_pdf(pdf_path, pages=str(page_num+1))
#         except:
#             pass

#         # Get text blocks (with positions)
#         blocks = page.get_text("blocks")

#         # Store table bboxes (approx)
#         table_areas = []
#         for table in tables:
#             if hasattr(table, "_bbox"):
#                 table_areas.append(table._bbox)

#         # Filter text (remove table-like regions)
#         clean_text = ""
#         for block in blocks:
#             x0, y0, x1, y1, text, *_ = block

#             is_table_text = False
#             for area in table_areas:
#                 tx0, ty0, tx1, ty1 = area
#                 if (x0 >= tx0 and x1 <= tx1):
#                     is_table_text = True
#                     break

#             if not is_table_text:
#                 clean_text += text + "\n"

#         combined_text += clean_text

#         # Now add table ONLY ONCE
#         for i, table in enumerate(tables):
#             combined_text += f"\n--- Table {i+1} (Page {page_num+1}) ---\n"
#             combined_text += table.df.to_string()
#             combined_text += "\n"

#     return combined_text




import fitz
import camelot

def process_pdf(pdf_path):

    doc = fitz.open(pdf_path)
    combined_text = ""

    for page_num in range(len(doc)):

        combined_text += f"\n--- Page {page_num+1} Text ---\n"

        page = doc.load_page(page_num)

        # Extract tables first
        tables = []
        try:
            tables = camelot.read_pdf(pdf_path, pages=str(page_num+1))
        except:
            pass

        # Get text blocks (with positions)
        blocks = page.get_text("blocks")

        # Store table bboxes (approx)
        table_areas = []
        for table in tables:
            if hasattr(table, "_bbox"):
                table_areas.append(table._bbox)

        # Filter text (remove table-like regions)
        clean_text = ""
        for block in blocks:
            x0, y0, x1, y1, text, *_ = block

            is_table_text = False
            for area in table_areas:
                tx0, ty0, tx1, ty1 = area
                if (x0 >= tx0 and x1 <= tx1):
                    is_table_text = True
                    break

            if not is_table_text:
                clean_text += text + "\n"

        combined_text += clean_text

        # Now add table ONLY ONCE
        for i, table in enumerate(tables):
            combined_text += f"\n--- Table {i+1} (Page {page_num+1}) ---\n"
            combined_text += table.df.to_string()
            combined_text += "\n"

    return combined_text

