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

operations = get_load_data(operations_file)
def get_filtered(operations):
    """
    Функция возвращает отфильтрованные транзакции по статусу - Выполнено
    """
    executed_operations = [op for op in operations if op.get("state") == "EXECUTED"]

    return executed_operations


sorting_file = get_filtered(operations)
def get_sort_date(sorting_file):
    """Функция возвращает транзакции сортированные по дате в обратном порядке"""

    executed_sorted = sorted(sorting_file, key=lambda op: datetime.fromisoformat(op['date']), reverse=True)

    return executed_sorted


def get_format_summ(money):
    """Функция возвращает сумму и валюту транзакции"""
    amount = float(money['operationAmount']['amount'])
    currency_name = money['operationAmount']['currency']["name"]
    return f'{amount} {currency_name}'


print(get_load_data(operations_file))
print(get_change_date_format("2019-02-01T00:00:00.000001"))
print(mask_card_or_account("Maestro 4598300720424501"))
print(get_filtered(operations))
print(get_sort_date(sorting_file))
