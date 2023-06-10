import json


def load_operations():
    """ Загружает json файл """

    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def executed_operations():
    """ Возвращает отфильтрованный список ВЫПОЛНЕННЫХ операций """
    ex_operations = []
    for i in load_operations():
        try:
            if i['state'] == 'EXECUTED':
                ex_operations.append(i)
        except KeyError:
            continue
    return ex_operations


def show_last_five():
    """ Возвращает список из пяти последних выполненных операций, отсортированных по датам (сначала самые последние) """

    sorted_list = executed_operations()
    for i in sorted_list:
        # изменяет формат даты
        i['date'] = "".join(i['date'].split('T')[0])
        sorted_list = sorted(sorted_list, key=lambda x: x['date'], reverse=True)

    return sorted_list[:5]


def show_account(num):
    """ Возвращает замаскированный формат карты или счета """

    num_split = num.split()
    account = num_split[-1]
    name = num[0:len(num) - len(account)]
    if len(account) == 16:
        # это карта
        account = account[:4] + " " + account[4:6] + "**" + " " + "****" + " " + account[-4:]
    else:
        # это счет
        account = "**" + account[-4:]
    return name + account
