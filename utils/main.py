from utils.func import (get_load_data, get_change_date_format, mask_card_or_account,
                        get_filtered, get_sort_date, get_format_summ, operations_file)

from colorama import Fore, Style


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
        if operation["description"] != "Открытие вклада":
            print(mask_card_or_account(operation["from"]) + " -> ", end="")
        print(mask_card_or_account(operation["to"]))
        print(get_format_summ(operation))


if __name__ == '__main__':
    main()
