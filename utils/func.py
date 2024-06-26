import json
from datetime import datetime

from colorama import Fore, Style


def get_load_data(file_name):
    """
    Функция возвращает список, загружая и читая файл с транзакциями
    """
    with open(file_name, 'r') as f:
        return json.load(f)


def get_change_date_format(date):
    """
    Функция возвращает преобразованную дату в нужный формат
    """
    return datetime.fromisoformat(date).strftime(Fore.RED + '%d.%m' + Style.RESET_ALL + '.%Y')


def mask_card_or_account(value):
    """
    Функция маскирует номер карты или счета.
    """
    nums = value.split()
    number = nums[-1]
    red = Fore.RED
    clear = Style.RESET_ALL
    if nums[0] == "Счет":
        return f"Счет **{number[-4:]}"
    else:
        card_name = ' '.join(nums[:-1])
        return f"{card_name} {red}{number[:4]} {number[4:6]}{clear}** **** {red}{number[-4:]}{clear}"


def get_filtered(operations):
    """
    Функция возвращает отфильтрованные транзакции по статусу - Выполнено
    """
    executed_operations = [op for op in operations if op.get("state") == "EXECUTED"]
    return executed_operations


def get_sort_date(sorting_file):
    """
    Функция возвращает транзакции сортированные по дате в обратном порядке
    """
    executed_sorted = sorted(sorting_file, key=lambda op: datetime.fromisoformat(op['date']), reverse=True)
    return executed_sorted


def get_format_summ(money):
    """
    Функция возвращает сумму и валюту транзакции
    """
    amount = float(money['operationAmount']['amount'])
    currency_name = money['operationAmount']['currency']["name"]
    return f'{Fore.RED}{amount} {Style.RESET_ALL}{currency_name}'
