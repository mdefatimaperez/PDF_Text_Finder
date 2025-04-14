import PyPDF2
import os.path
import sys
import re

def extract_text_from_pdf(pdf_file: str) -> list[str]:

    if not os.path.isfile(pdf_file):
        print(f"Error: File '{pdf_file}' not found.")
        return []

    try:
        with open(pdf_file, 'rb') as pdf:
            reader = PyPDF2.PdfReader(pdf)
            pdf_text = []

            for page in reader.pages:
                content = page.extract_text()
                pdf_text.append(content)

            return pdf_text
    except Exception as e:
        print(f"Error processing PDF '{pdf_file}': {e}")
        return []


if __name__ == "__main__":
    pdf_filename = 'pdf_to_text.pdf' # Replace with your PDF file name!
    extracted_text_list = extract_text_from_pdf(pdf_filename)

    if not extracted_text_list:
        print("Could not extract text or file not found.")
        sys.exit(1)

    print(f"\n--- Searching for the word 'Shrek' in '{pdf_filename}' ---")
    found_on_pages = []
    shrek_count = 0

    for page_num, text in enumerate(extracted_text_list, start=1):
        if text and "Shrek" in text:

            paragraph_placeholder = "___PARAGRAPH_BREAK___"
            processed_text = re.sub(r'\n{2,}', paragraph_placeholder, text)
            processed_text = processed_text.replace('\n', ' ')
            cleaned_text = processed_text.replace(paragraph_placeholder, '\n\n')
            cleaned_text = re.sub(' +', ' ', cleaned_text).strip()

            shrek_count += cleaned_text.lower().count("shrek")
            print(f"\n--- Content of Page {page_num} (contains the word 'Shrek') ---")
            print(cleaned_text)
            print("=" * 50)
            print(f"Occurrences of the word 'Shrek' on this page: {cleaned_text.lower().count('shrek')}")
            found_on_pages.append(page_num)

    if found_on_pages:
        print(f"\nSummary: The word 'Shrek' was found on pages: {found_on_pages}")
    else:
        print("\nSummary: The word 'Shrek' was not found on any page.")