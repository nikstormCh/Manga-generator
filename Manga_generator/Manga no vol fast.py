from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os
import re
import concurrent.futures

def natural_sort_key(s):
    return [
        int(text) if text.isdigit() else text.lower()
        for text in re.split('([0-9]+)', s)
    ]

# Single function to handle a single chapter -> PDF
def process_chapter(index_and_paths):
    index, chapter, base_path, save_directory = index_and_paths
    chapter_path = os.path.join(base_path, chapter)

    # Get all image files
    image_files = [
        f for f in os.listdir(chapter_path)
        if f.lower().endswith(('.png', '.jpg', '.jpeg'))
    ]
    image_files = sorted(image_files, key=natural_sort_key)

    # If no images, skip
    if not image_files:
        return f"No images in {chapter}"

    pdf_file_name = f"Fire Force Chapter {index}.pdf"
    pdf_full_path = os.path.join(save_directory, pdf_file_name)

    # Create the PDF
    c = canvas.Canvas(pdf_full_path, pagesize=letter)

    page_width, page_height = letter
    for image_file in image_files:
        image_path = os.path.join(chapter_path, image_file)
        img = Image.open(image_path)

        # Calculate scale
        img_width, img_height = img.size
        ratio = min(page_width / img_width, page_height / img_height)
        new_width = img_width * ratio
        new_height = img_height * ratio

        x = (page_width - new_width) / 2
        y = (page_height - new_height) / 2

        c.drawImage(image_path, x, y, width=new_width, height=new_height)
        c.showPage()

    c.save()
    return f"PDF file '{pdf_file_name}' created successfully."

# -------------------------------------------------------------------------
if __name__ == "__main__":
    base_path = r"C:\Users\nikst\Downloads\Enen no Shouboutai"
    save_directory = r"C:\Users\nikst\Desktop\manga\Manga_generator"

    # Get all chapter folders
    chapters = [
        folder for folder in os.listdir(base_path)
        if os.path.isdir(os.path.join(base_path, folder))
    ]
    chapters = sorted(chapters, key=natural_sort_key)

    # Prepare data for parallel processing
    index_chapter_list = [(i+1, chap, base_path, save_directory)
                          for i, chap in enumerate(chapters)]

    # Use up to N processes (or threads).
    # For CPU-bound tasks, ProcessPoolExecutor is often faster.
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(process_chapter, data)
                   for data in index_chapter_list]

        for future in concurrent.futures.as_completed(futures):
            print(future.result())
