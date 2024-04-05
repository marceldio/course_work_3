import json
from datetime import datetime
import os
from config import ROOT_DIR

operations_file = os.path.join(ROOT_DIR, 'utils', 'operations.json')


def get_load_data(file_name):
    """Функция возвращает список, загружая и читая файл с транзакциями"""

    with open(file_name, 'r') as f:
        return json.load(f)


def get_change_date_format(date):
    """Функция возвращает преобразованную дату в нужный формат"""

    return datetime.fromisoformat(date).strftime('%d.%m.%Y')

print(get_load_data(operations_file))
print(get_change_date_format("2019-02-01T00:00:00.000001"))
