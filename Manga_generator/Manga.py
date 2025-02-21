from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os
import re


def natural_sort_key(s):
    """
    Возвращает ключ для сортировки, который преобразует строку в кортеж,
    содержащий числа в строке как целые числа и остальные части как текст.
    """
    return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]


base_path = r"C:\Users\nikst\Downloads\Enen no Shouboutai"

vols = os.listdir(base_path)
vols = sorted(vols, key=natural_sort_key)

folder_names_2d = []
path_to_vols = ""
for i in vols:
    path_to_vols = os.path.join(base_path, i)
    folder_names_2d.append(sorted(os.listdir(path_to_vols), key=natural_sort_key))

index = 1
print(f"index = {index}")
save_directory = r"C:\Users\nikst\Desktop\manga\Manga_generator"

path_to_images = ""
for folder_names in path_to_vols:
    """folder_names_2d^^^"""
    pdf_file_name = f"Fire force {index}.pdf"
    pdf_full_path = os.path.join(save_directory, pdf_file_name)
    c = canvas.Canvas(pdf_full_path, pagesize=letter)
    for name in folder_names:
        path_to_images = ""
        path_to_images = os.path.join(base_path, vols[index - 1])
        path_to_images = os.path.join(path_to_images, name)

        files = sorted([f for f in os.listdir(path_to_images) if f.endswith('.png') or f.endswith('.jpg')])
        files = sorted(files, key=natural_sort_key)
        for file in files:
            path = os.path.join(path_to_images, file)
            img = Image.open(path)

            width, height = letter
            img_width, img_height = img.size
            ratio = min(width / img_width, height / img_height)
            img_width_new, img_height_new = img_width * ratio, img_height * ratio

            x = (width - img_width_new) / 2
            y = (height - img_height_new) / 2

            c.drawImage(path, x, y, width=img_width_new, height=img_height_new)
            c.showPage()
            print(f'добавлена страница {file} из папки {name}')
    c.save()
    print(f"PDF файл {pdf_file_name} успешно создан.")
    index += 1
    print(f"index = {index}")
