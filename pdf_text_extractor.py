# pdf_text_extractor.py
"""
This module extracts text from PDF files.
We use PyPDF2 for text extraction with page-wise handling.
"""

import PyPDF2
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
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            total_pages = len(pdf_reader.pages)
            print(f"[INFO] Total pages found: {total_pages}")
            
            for page_number in range(total_pages):
                page = pdf_reader.pages[page_number]
                text = page.extract_text()
                
                if text:
                    full_text += f"\n\n[Page {page_number + 1}]\n{text}"
                else:
                    print(f"[WARNING] No text found on Page {page_number + 1}")

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