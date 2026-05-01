import pdfplumber

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        # pdfplumber is significantly smarter at reading 2-column resumes
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                # x_tolerance and y_tolerance prevent words from getting mashed together
                extracted = page.extract_text(x_tolerance=2, y_tolerance=3)
                if extracted:
                    text += extracted + "\n"
    except Exception as e:
        print(f"Extraction Error: {e}")
        
    return text