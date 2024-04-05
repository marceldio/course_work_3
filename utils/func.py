import json
from datetime import datetime
import os
from config import ROOT_DIR

operations_file = os.path.join(ROOT_DIR, 'utils', 'operations.json')


def get_load_data(file_name):
    """Функция возвращает список, загружая и читая файл с транзакциями"""

    with open(file_name, 'r') as f:
        return json.load(f)
