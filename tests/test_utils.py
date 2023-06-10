from src.utils import show_account


def test_utils():
    assert show_account('Счет 77613226829885488381') == 'Счет **8381'
    assert show_account('Visa Gold 7756673469642839') == 'Visa Gold 7756 67** **** 2839'

