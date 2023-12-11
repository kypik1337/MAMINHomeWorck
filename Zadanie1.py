# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее файла новый с данными в Задание №1 формате JSON.
# Имена пишите с большой буквы. Каждую пару сохраняйте с новой строки.


import json
from pathlib import Path


def convert(path: Path) -> None:
    my_dict = {}
    with open(name, 'r', encoding='usf-8') as f:
        for line in f:
            name, number = line.split('')
            my_dict[name.title()] = float(number)
    with open(f'{name.stem}.json', 'w', encoding='utf-8'):
        json.dump(my_dict, f, indent=2, ensure_ascii=False)



if __name__ == '__main__':
    convert(Path('result.txt'))



