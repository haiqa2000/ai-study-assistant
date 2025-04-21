# pdf_text_extractor.py
"""
This module extracts text from PDF files.
We use pdfplumber for accurate text extraction with page-wise handling.
"""

import pdfplumber
import os

def extract_text_from_pdf(pdf_path):
    """
    Extracts text content from a given PDF file.
    
    Parameters:
    - pdf_path (str): Full path to the PDF file.
    
    Returns:
    - full_text (str): All extracted text from the PDF.
    """
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"File not found: {pdf_path}")

    full_text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            print(f"[INFO] Total pages found: {len(pdf)}")
            for page_number, page in enumerate(pdf, start=1):
                text = page.extract_text()
                if text:
                    full_text += f"\n\n[Page {page_number}]\n{text}"
                else:
                    print(f"[WARNING] No text found on Page {page_number}")

        return full_text.strip()

    except Exception as e:
        print(f"[ERROR] Failed to extract text from PDF: {e}")
        return None

# Test script (only runs if this file is executed directly)
if __name__ == "__main__":
    test_pdf_path = input("Enter the full path to your PDF file: ")
    extracted_text = extract_text_from_pdf(test_pdf_path)

    if extracted_text:
        print("\n[EXTRACTED TEXT]\n", extracted_text[:500], "...\n")  # print only first 500 characters
    else:
        print("[ERROR] Could not extract text.")
