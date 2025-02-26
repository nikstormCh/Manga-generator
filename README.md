Manga Generator

1. Overview:
Manga Generator is a Python-based tool that automates the process of converting manga image files into properly sorted and formatted PDF files. It supports multi-volume manga collections and efficiently processes entire directories of manga chapters. The project is designed for users who want to convert manga images into easy-to-read PDF documents while preserving the correct reading order.

2. Features:
* Batch extraction of manga archives from ZIP files.
* Automatic sorting of chapters and pages using natural sorting logic.
* Conversion of manga images (.jpg, .jpeg, .png) into formatted PDF files.
* Multi-threaded processing for faster conversion of multiple chapters.
* Full-volume support for organizing manga collections.

3. Installation:
Prerequisites
Ensure you have the following installed:
Python 3.x
Required dependencies:
pip install pillow reportlab

4. Project Structure:

Manga-Generator/
│── extractor.py            # Extracts manga ZIP archives
│── Manga.py                # Processes full volumes into PDFs
│── Manga no vol.py         # Processes single chapters into PDFs (single-threaded)
│── Manga no vol fast.py    # Multi-threaded version of the chapter processor
│── massiv.py               # Lists and sorts available chapters
│── README.md               # Project documentation

5. Usage:

Extracting Manga Archives

Ensure .zip files are placed in the correct directory. Run:

python extractor.py

This script will extract all .zip archives into the working directory.

Generating PDFs

Convert Full Manga Volumes to PDFs

Run:

python Manga.py

This script:

Iterates through all volumes in the base folder.

Sorts and converts images to PDF format.

Saves them as Fire Force Volume X.pdf.

Convert Single Chapters to PDFs

Run:

python Manga no vol.py

This script:

Processes individual manga chapters.

Outputs PDFs as Fire Force Chapter X.pdf.

Faster Processing with Multi-threading

Run:

python Manga no vol fast.py

This script:

Uses multi-threading to speed up conversion.

Converts chapters in parallel for efficiency.

Checking Available Chapters

To list available manga folders, run:

python massiv.py

This script prints a list of available chapter folders.
