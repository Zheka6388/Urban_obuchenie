import os  # Импортируем модуль os для работы с файловой системой
import time  # Импортируем модуль time для работы с временем

directory = "." # Указываем директорию для обхода (текущая директория)

for root, dirs, files in os.walk(directory): # Обходим директорию с помощью os.walk
    for file in files: # Перебираем все файлы в текущем каталоге
        filepath = os.path.join(root, file) # Формируем полный путь к файлу
        filetime = os.path.getmtime(filepath) # Получаем время последнего изменения файла
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))  # Форматируем время
        filesize = os.path.getsize(filepath) # Получаем размер файла в байтах
        parent_dir = os.path.dirname(filepath) # Получаем родительскую директорию файла


    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения:'
      f' {formatted_time},Родительская директория: {parent_dir}') # Выводим информацию о файле
