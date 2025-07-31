# PDF Auditor

## Project Description
PDF Auditor is a desktop tool designed for accessibility teams and website owners to automate end-to-end compliance checks on PDFs published on public websites. It combines web scraping, PDF retrieval, and accessibility analysis (PDF/UA and WCAG 2.1) in a user-friendly GUI, generating Excel reports of results.

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone https://github.com/<your-username>/pdf_auditor.git
   cd pdf_auditor
   ```
2. **Create and activate a virtual environment (Windows):**
   ```
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

## Usage Examples

- **Run the application:**
  ```
  python src/pdf_auditor/gui/main.py
  ```
- **Basic workflow:**
  1. Enter the target website URL in the GUI.
  2. Specify the download directory for PDFs.
  3. Start the scan to discover and download PDFs.
  4. View accessibility analysis results in the GUI.
  5. Export results to Excel for reporting.

For more details, see the user documentation in the `docs/` folder.
