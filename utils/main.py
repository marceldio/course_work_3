from utils.func import (get_load_data, get_change_date_format, mask_card_or_account,
                        get_filtered, get_sort_date, get_format_summ)
from colorama import Fore, Style
from config import operations_file


def main():
    """
    Основная функция - выводит детали последних 5 транзакций.,
    """
    loaded_file = get_load_data(operations_file)
    executed_operations = get_filtered(loaded_file)
    sorted_operations = get_sort_date(executed_operations)

    for i, operation in enumerate(sorted_operations[:5]):
        if i > 0:
            print()

        print(get_change_date_format(operation["date"]), operation["description"])
        if operation.get("from"):
            print(mask_card_or_account(operation["from"]) + " -" + Fore.RED + "> " + Style.RESET_ALL, end="")
        print(mask_card_or_account(operation["to"]))
        print(get_format_summ(operation))


if __name__ == '__main__':
    main()
