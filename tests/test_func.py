from utils.func import get_load_data
import os
import pytest
from config import ROOT_DIR

test_file = os.path.join(ROOT_DIR, 'tests', 'test_operations.json')


def test_get_load_data():
    """Тест функции которая загружат и читает  json - файл"""

    assert get_load_data(test_file) == [{"1": 1, "2": 2, "3": "three"}]


