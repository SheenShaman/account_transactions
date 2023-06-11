import json
import os

operations_json = os.path.join('/home', 'sheen', 'account_transactions', 'src', 'operations.json')


def load_operations(operations):
    """ Загружает json файл """
    with open(operations, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def executed_operations():
    """ Возвращает отфильтрованный список ПОСЛЕДНИХ ПЯТИ ВЫПОЛНЕННЫХ операций """

    ex_operations = [item for item in load_operations(operations_json) if item.get('state') == 'EXECUTED']
    for i in ex_operations:
        # изменяет формат даты
        i['date'] = "".join(i['date'].split('T')[0])
    ex_operations = sorted(ex_operations, key=lambda x: x['date'], reverse=True)

    return ex_operations[:5]


def show_account(num):
    """ Возвращает замаскированный формат карты или счета """

    num_split = num.split()
    account = num_split[-1]
    name = num[0:len(num) - len(account)]
    if len(account) == 16:
        # это карта
        account = account[:4] + " " + account[4:6] + "** **** " + account[-4:]
    else:
        # это счет
        account = "**" + account[-4:]
    return name + account
