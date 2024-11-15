import os
import time

# Указываем директорию для обхода
directory = "."

# 1
for root, dirs, files in os.walk(directory):
    for file in files:
        # 2
        filepath = os.path.join(root, file)
        # 3
        filetime = os.path.getmtime(filepath)
        # 3.1
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        # 4
        filesize = os.path.getsize(filepath)
        # 5
        parent_dir = os.path.dirname(filepath)

        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time},'
            f' Родительская директория: {parent_dir}')
