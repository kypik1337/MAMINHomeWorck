from Zadanie1 import convert
from ZAdanie2 import set_user
from Zadanie4 import csv_to_json
from Zadanie6 import pickle_to_csv


# 2. Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
# import os
# import json
# import csv
# import pickle


# def prodect_folder(directory: str) :
#     result = []
#     for root, dir, file in os.walk(directory):
#         dir_size = 0
#         for fil in file:
#             file_path = os.path.join(root, file)
#             size = os.path.getsize(file_path)
#             dir_size += size
#             result.append({'path': file_path, 'type': 'size', 'size': size, 'parent_directory': root })
#         result.append({'path': root, 'type': 'directory', 'size': dir_size, 'perrants_directory': os.path.dirname(root)})
#     with open('result.json', 'w') as json_file:
#         json.dump(result, json_file, indent=1)
#     with open('result.csv', 'w', newline='') as csv_file:
#         write_inf = csv.DictWriter(csv_file, fieldnames=['path', 'type', 'size', 'parent_directory'])
#         write_inf.writeheader()
#         write_inf.writerows(result)
#     with open('result.pickle', 'wb') as pickle_file:
#         pickle.dump(result, pickle_file)


# if __name__ == '__main__':
#     prodect_folder(':/Users/artem/Library/Mobile Documents/com~apple~CloudDocs/Worck')


# 3. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.


convert('result.txt') # .txt
set_user('result.json') # .json
csv_to_json('users.csv') # .csv
pickle_to_csv('new_users.pickle') # .pickle
print('Winners')










