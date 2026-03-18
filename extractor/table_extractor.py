#handles table extraction uses camelot
#pdf -> detect tables -> convert to text
import camelot


def extract_tables(pdf_path):

    table_text = ""

    try:
        tables = camelot.read_pdf(pdf_path, pages="all")

        for i, table in enumerate(tables):

            table_text += f"\n--- Table {i+1} ---\n"
            table_text += table.df.to_string()

    except Exception as e:

        table_text += "\nNo tables detected.\n"

    return table_text