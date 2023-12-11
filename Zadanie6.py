
import json 
import pickle
from pathlib import Path
import csv


def pickle_to_csv(file: Path) -> None:
    with (
        open(file, 'rb') as f_read,
        open(f'{file.stem}.csv', 'w', encoding='utf-8', newline='') as f_write
    ):
        data = pickle.load(f_read)
        headers_list = list(data[0].keys())
        csv_write = csv.DictWriter(f_write, fieldnames=headers_list, dialect='exel-tab', quotechar=csv.QUOTE_NONNUMERIC)
        csv_write.writeheader()
        csv_write.writerows(data)
if __name__ == '__main__':
    pickle_to_csv(Path('new_users.pickle'))









