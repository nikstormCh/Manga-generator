import os

# Задаём путь к конкретной директории
directory_path = r"C:\Users\nikst\Downloads\Enen no Shouboutai"

# Получаем список всех объектов в директории
all_objects = os.listdir(directory_path)

# Инициализируем пустой список для названий папок
folders = []

# Проходим по всем объектам и добавляем названия папок в список
for obj in all_objects:
    # Формируем полный путь к объекту
    full_path = os.path.join(directory_path, obj)

    # Если объект является папкой, добавляем его название в список
    if os.path.isdir(full_path):
        folders.append(obj)

# Выводим список папок
print(folders)
