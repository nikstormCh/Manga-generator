import os
import zipfile

# Путь к директории с ZIP-файлами
directory_path = 'Volume 16'

# Проходим по всем файлам в указанной директории
for filename in os.listdir(directory_path):
    # Проверяем, является ли файл ZIP-архивом
    if filename.endswith('.zip'):
        # Формируем полный путь к ZIP-файлу
        zip_path = os.path.join(directory_path, filename)
        # Создаём объект ZipFile
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # Извлекаем все содержимое архива в директорию directory_path
            zip_ref.extractall(directory_path)

print("Все ZIP-файлы были успешно разархивированы.")
