# from extractor.pdf_processor import process_pdf
# from config import INPUT_FILE, OUTPUT_FILE
# from utils.file_utils import save_text
# from agents.validator_agent import validate_sow


# def main():

#     print("Starting PDF processing...")

#     extracted_text = process_pdf(INPUT_FILE)

#     print("Sending text to Validator Agent...")

#     validation_result = validate_sow(extracted_text)

#     save_text(validation_result, OUTPUT_FILE)

#     print("Validation completed!")


# if __name__ == "__main__":
#     main()
    


from extractor.pdf_processor import process_pdf
from config import INPUT_FILE, OUTPUT_FILE
from utils.file_utils import save_text

def main():

    print("Starting PDF processing...")

    extracted_text = process_pdf(INPUT_FILE)

    save_text(extracted_text, OUTPUT_FILE)

    print("Extraction completed!")

if __name__ == "__main__":
    main()