###PDF Text Finder 📄🔍
A simple Python script to extract text from PDF files, clean it for better console readability, and search for a specific keyword.
<br>
---
##📜 Description
This project is a straightforward command-line tool that:
Opens a user-specified PDF file.
Extracts the text content from each page using the PyPDF2 library.
Processes the extracted text to attempt formatting it into more readable paragraphs by handling unnecessary line breaks.
Searches for a user-defined keyword (case-insensitive for counting, case-sensitive for initial check) within the text of each page. The example uses "Shrek", but you can change it!
Prints the processed content of pages where the keyword was found to the console, along with the page number and the count of occurrences on that page.
Displays a final summary indicating which pages contained the keyword.
It serves as a practical example of working with PDFs in Python and performing customizable text searches.
<br>
---
✨ Features
Reads PDF files.
Extracts text on a page-by-page basis.
Basic text cleaning to improve console readability (handles line breaks).
Configurable Search: Easily change the keyword to search for.
Counts keyword occurrences per page.
Provides clear console output showing results per page and a final summary.
<br>
---
⚙️ Prerequisites
You will need the following installed on your system:
Python 3: Python 3.6 or higher is recommended. You can download it from python.org.
pip: The Python package installer (usually comes with Python).
<br>
---
🚀 Installation
Clone the repository:
git clone <YOUR_REPO_URL_HERE>
cd <REPO_DIRECTORY_NAME>
Use code with caution.
Bash
(Replace <YOUR_REPO_URL_HERE> with the actual URL of your repository and <REPO_DIRECTORY_NAME> with the name of the created directory).
Install dependencies:
This project requires the PyPDF2 library. Install it using pip:
pip install PyPDF2
Use code with caution.
Bash
(If you are using a virtual environment (recommended), make sure it's activated before running this command).
<br>
---
📋 Usage
Prepare your PDF file:
Place any PDF file you want to analyze in the same directory as the Python script (pdf_lector.py or whatever you named it).
You can use the pdf_to_text.pdf file included in this repository as an initial example.
Configure the script:
Open the Python script file (pdf_lector.py) in a text editor.
To change the PDF file to analyze:
Find the line:
pdf_filename = 'pdf_to_text.pdf' # Change this to your PDF file name!
Use code with caution.
Python
Replace 'pdf_to_text.pdf' with the exact name of your PDF file (e.g., 'my_document.pdf').
To change the keyword to search for:
Find the lines where "Shrek" (or the current keyword) is used. They are inside the for page_num, text... loop:
# Inside the if condition:
if text and "Shrek" in text: # <-- Change "Shrek" here

# Inside the counter calculation:
shrek_count += cleaned_text.lower().count("shrek") # <-- Change "shrek" here (lowercase)

# Inside the count print message:
print(f"Occurrences of the word 'Shrek' on this page: {cleaned_text.lower().count('shrek')}") # <-- Change 'Shrek' and 'shrek' here
Use code with caution.
<br>
---
***Python
Replace "Shrek" (and "shrek" in lowercase where applicable) with the word or phrase you want to search for. Remember the in check is case-sensitive, but the .count() is performed on the lowercased text!
Save the changes to the script file.
Run the script:
Open your terminal or command line.
Make sure you are in the project directory.
Execute the script using Python:
python pdf_lector.py
Use code with caution.
<br>
---
***Bash
(Replace pdf_lector.py if you named your .py file differently)
Review the output:
The script will print the pages containing the keyword you defined to the console, displaying the processed text and the occurrence count for that page.
At the end, you will see a summary listing all pages where the keyword was found.
<br>
---
***📝 Note on Text Extraction
The quality of text extracted from a PDF can vary greatly depending on how the original PDF was created. This script uses PyPDF2, which works well for many text-based PDFs but may struggle with:
PDFs that are scanned images (would require OCR - Optical Character Recognition).
PDFs with complex formatting, tables, or unusual layouts.
Password-protected or encrypted PDFs.
The implemented text cleaning helps with common line break issues but might not be perfect for all documents.
