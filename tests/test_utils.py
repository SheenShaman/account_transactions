import os
from src.utils import load_operations, executed_operations, show_account

# путь до файлов json
cwd = os.path.abspath('.')
data_test = os.path.join(os.path.dirname(__file__), 'data_test.json')
executed_data_test = os.path.join(os.path.dirname(__file__), 'executed_data_test.json')

# ожидаемые выводы
result_data_test = [
        {
            "id": 863064926,
            "state": "EXECUTED",
            "date": "2019-12-08T22:46:21.935582"
        },
        {
            "id": 560813069,
            "state": "CANCELED",
            "date": "2019-12-03T04:27:03.427014"
        },
        {
            "id": 114832369,
            "state": "EXECUTED",
            "date": "2019-12-07T06:17:14.634890"
        },
        {
            "id": 482520625,
            "state": "EXECUTED",
            "date": "2019-11-13T17:38:04.800051"
        },
        {
            "id": 801684332,
            "state": "EXECUTED",
            "date": "2019-11-05T12:04:13.781725"
        }
    ]
result_ex_data_test = [
  {
    "id": 863064926,
    "state": "EXECUTED",
    "date": "2019-12-08"
  },
  {
    "id": 114832369,
    "state": "EXECUTED",
    "date": "2019-12-07"
  },
  {
    "id": 154927927,
    "state": "EXECUTED",
    "date": "2019-11-19"
  },
  {
    "id": 482520625,
    "state": "EXECUTED",
    "date": "2019-11-13"
  },
  {
    "id": 801684332,
    "state": "EXECUTED",
    "date": "2019-11-05"
  }
]


def test_load_operations():
    assert load_operations(data_test) == result_data_test


def test_executed_operations():
    assert executed_operations(load_operations(executed_data_test)) == result_ex_data_test


def test_show_account():
    assert show_account('Счет 77613226829885488381') == 'Счет **8381'
    assert show_account('Visa Gold 7756673469642839') == 'Visa Gold 7756 67** **** 2839'
