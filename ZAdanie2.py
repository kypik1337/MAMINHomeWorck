import json
from pathlib import Path


def set_user(file: Path) -> None:
    u_ids = set()
    if not file.is_file():
        data = {i: {} for i in range(1, 7 +1)}
    else:
        with open(file, 'r', encoding='utf-8') as f:
            data = json.loads(f)
        for value in data.values():
            u_ids.update(value.keys())
    while True:
        name = input('Введите имя: ')
        if not name:
            break
        id = int(input('Введите id: '))
        lvl = input('Введите уровень от 1 до 7: ')
        if ~ (id in u_ids and data[lvl].get(id) is None):
            data[lvl].update({id: name})
            with open(file, 'w', encoding='utf-8') as f_write:
                json.dump(data, f_write, indent=2, ensure_ascii=False)



if __name__ == '__main__':
    set_user(Path('users.json'))





