from utils.func import (get_load_data, get_change_date_format, mask_card_or_account,
                        get_filtered, get_sort_date, get_format_summ)
import os
import pytest
from config import ROOT_DIR
from colorama import Fore, Style

test_file = os.path.join(ROOT_DIR, 'tests', 'test_operations.json')

test_op = [
  {"id": 1, "state": "EXECUTED", "date": "2018-06-01T00:00:00.000000"},
  {"id": 2, "state": "CANCELED", "date": "2018-02-01T00:00:00.000000"},
  {"id": 3, "state": "EXECUTED", "date": "2018-03-01T00:00:00.000000"},
  {"id": 4, "state": "EXECUTED", "date": "2018-01-01T00:00:00.000001"}
]


@pytest.fixture
def test_op_fixture():
    return test_op


def test_get_load_data():
    """
    Тест функции которая загружат и читает  json-файл
    """
    assert get_load_data(test_file) == [{"1": 1, "2": 2, "3": "three"}]


def test_get_change_date_format():
    """
    Тест функции которая преобразует формат даты
    """
    assert get_change_date_format("2019-02-01T00:00:00.000001") == Fore.RED + "01.02" + Style.RESET_ALL + ".2019"


def test_mask_card_or_account():
    """
    Тест функции которая маскирует номер карты или счета.
    """
    assert mask_card_or_account("Maestro "
                                "4598300720424501") == ("Maestro "
                                                        + Fore.RED + "4598 30"
                                                        + Style.RESET_ALL + "** **** "
                                                        + Fore.RED + "4501" + Style.RESET_ALL)
    assert mask_card_or_account("Счет 27248529432547658655") == "Счет **8655"


def test_get_filtered(test_op_fixture):
    """
    Тест функции которая фильтрует транзакции по статусу - Выполнено
    """
    assert len(get_filtered(test_op_fixture)) == 3


def test_get_sort_date(test_op_fixture):
    """
    Тест функции которая возвращает транзакции сортированные по дате в обратном порядке
    """
    assert [i["id"] for i in get_sort_date(test_op_fixture)] == [1, 3, 2, 4]


def test_get_format_summ():
    """
    Тест функции которая возвращает сумму и валюту транзакции
    """
    data = {
        "id": 104807525,
        "state": "EXECUTED",
        "date": "2019-06-01T06:46:16.803326",
        "operationAmount": {
          "amount": "60888.63",
          "currency": {
            "name": "руб.",
            "code": "RUB"
          }
        },
        "description": "Перевод с карты на счет",
        "from": "МИР 8201420097886664",
        "to": "Счет 35116633516390079956"
    }
    assert get_format_summ(data) == Fore.RED + "60888.63 " + Style.RESET_ALL + "руб."
