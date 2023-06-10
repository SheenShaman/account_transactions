from src.utils import load_operations, executed_operations, show_account


def test_load_operations():
    from_file = [
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
    assert load_operations('/home/sheen/account_transactions/src/data_test.json') == from_file


def test_executed_operations():
    pass


def test_utils():
    assert show_account('Счет 77613226829885488381') == 'Счет **8381'
    assert show_account('Visa Gold 7756673469642839') == 'Visa Gold 7756 67** **** 2839'
