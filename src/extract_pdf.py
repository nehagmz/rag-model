import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        text = text.encode('utf-8').decode('utf-8')  # Ensure proper encoding
        
        if not text.strip():
            raise ValueError("No extractable text found in the PDF.")
        
        return text
    except Exception as e:
        raise RuntimeError(f"Error extracting text from PDF: {e}")
