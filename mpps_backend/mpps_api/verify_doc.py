import re
import pdfplumber

def verify_license(document_path, existing_licenses):
    with pdfplumber.open(document_path) as pdf:
        first_page = pdf.pages[0]
        text = first_page.extract_text()

    license_number = re.search(r'License Number: (\d+)', text)
    if license_number:
        license_number = license_number.group(1)
        if license_number in existing_licenses:
            return True
        else:
            return False
    else:
        return False