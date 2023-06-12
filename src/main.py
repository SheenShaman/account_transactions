import os
from src.utils import load_operations, executed_operations, show_account

# путь до файла json
cwd = os.path.abspath('.')
operations_json = os.path.join(cwd, 'operations.json')


def main():
    """ Выводит операции в нужном формате:
        <дата перевода> <описание перевода>
        <откуда> -> <куда>
        <сумма перевода> <валюта> """
    data = load_operations(operations_json)
    operations = executed_operations(data)
    for i in operations:
        date_op = i["date"].split('-')
        date_format = date_op[2] + '.' + date_op[1] + '.' + date_op[0]
        description_op = i["description"]
        to_op = show_account(i["to"])
        amount = i["operationAmount"]["amount"]
        currency_name = i["operationAmount"]["currency"]["name"]
        if "from" in i:
            from_op = show_account(i["from"])
        else:
            from_op = ""
        print(f"\n{date_format} {description_op}\n"
              f"{from_op} -> {to_op}\n"
              f"{amount} {currency_name}")


if __name__ == '__main__':
    main()
