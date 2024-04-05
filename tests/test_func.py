from utils.func import get_load_data, get_change_date_format, mask_card_or_account
import os
import pytest
from config import ROOT_DIR

test_file = os.path.join(ROOT_DIR, 'tests', 'test_operations.json')


def test_get_load_data():
    """Тест функции которая загружат и читает  json - файл"""

    assert get_load_data(test_file) == [{"1": 1, "2": 2, "3": "three"}]


def test_get_change_date_format():
    """Тест функции которая преобразует формат даты"""
    assert get_change_date_format("2019-02-01T00:00:00.000001") == "01.02.2019"


def test_mask_card_or_account():
    """Тест функции которая маскирует номер карты или счета."""
    assert mask_card_or_account("Maestro 4598300720424501") == "Maestro 4598 30** **** 4501"
    assert mask_card_or_account("Счет 27248529432547658655") == "Счет **8655"
