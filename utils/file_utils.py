#helper function   save text ad load file
#This saves the extracted text.
def save_text(text, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"Text successfully saved to {output_path}")