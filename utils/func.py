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


def mask_card_or_account(value):
  """
  Функция маскирует номер карты или счета.
  """
  nums = value.split()
  if nums[0] == "Счет":
    return "Счет **" + value[-4:]
  else:
    card_name = ' '.join(nums[:-1])
    return card_name + ' ' + nums[-1][:4] + ' ' + nums[-1][4:6] + '** **** ' + nums[-1][-4:]

print(get_load_data(operations_file))
print(get_change_date_format("2019-02-01T00:00:00.000001"))
print(mask_card_or_account("Maestro 4598300720424501"))
