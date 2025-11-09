import pdfplumber
import os
import io

def parse_pdf(pdf_path, output_path=None):
    """
    Parses a PDF file and extracts the text to a .txt file.

    Args:
        pdf_path (str): The path to the PDF file.
    """
    if not os.path.exists(pdf_path):
        print(f"Error: File not found at {pdf_path}")
        return


    with pdfplumber.open(pdf_path) as pdf, open(output_path, "w", encoding="utf-8") as f:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                f.write(text + '\n')
    print(f"Successfully converted {pdf_path} to {output_path}")