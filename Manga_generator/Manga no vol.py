from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os
import re


def natural_sort_key(s):
    """
    Returns a list of strings and integers that will be used
    to naturally sort names containing digits (e.g., chapter 2 vs chapter 10).
    """
    return [
        int(text) if text.isdigit() else text.lower()
        for text in re.split('([0-9]+)', s)
    ]


# 1. Main folder containing all chapter folders
base_path = r"C:\Users\nikst\Downloads\Enen no Shouboutai"

# 2. List all the chapters and sort them
chapters = [folder for folder in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, folder))]
chapters = sorted(chapters, key=natural_sort_key)

# 3. Where to save the resulting PDF files
save_directory = r"C:\Users\nikst\Desktop\manga\Manga_generator"

# 4. Iterate through each chapter folder
index = 1
for chapter in chapters:
    chapter_path = os.path.join(base_path, chapter)

    # Get all image files, then sort them naturally
    image_files = [f for f in os.listdir(chapter_path)
                   if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    image_files = sorted(image_files, key=natural_sort_key)

    if not image_files:
        continue  # Skip if no images found in this folder

    # Construct the PDF file name
    pdf_file_name = f"Fire Force Chapter {index}.pdf"
    pdf_full_path = os.path.join(save_directory, pdf_file_name)

    # Create a new PDF canvas for the chapter
    c = canvas.Canvas(pdf_full_path, pagesize=letter)

    # 5. Add each image to the PDF
    for image_file in image_files:
        image_path = os.path.join(chapter_path, image_file)
        img = Image.open(image_path)

        # Page size
        page_width, page_height = letter
        img_width, img_height = img.size

        # Scale the image to fit the page while maintaining aspect ratio
        ratio = min(page_width / img_width, page_height / img_height)
        new_width = img_width * ratio
        new_height = img_height * ratio

        # Center the image on the page
        x = (page_width - new_width) / 2
        y = (page_height - new_height) / 2

        c.drawImage(image_path, x, y, width=new_width, height=new_height)
        c.showPage()  # Move to the next PDF page
        print(f'Added page {image_file} from chapter {chapter}')

    # 6. Save the PDF for this chapter
    c.save()
    print(f"PDF file '{pdf_file_name}' successfully created.")

    index += 1
