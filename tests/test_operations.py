from utils import get_date, mask_from_to, get_filtered_and_sorted, prepare_user_msg


def test_get_date():
    assert get_date("2019-08-26T10:50:58.294041") == "26.08.2019"
    assert get_date("2018-03-23T10:45:06.972075") == "23.03.2018"


def test_mask_from_to():
    assert mask_from_to("Счет 64686473678894779589") == "Счет **9589"
    assert mask_from_to("Счет 38976430693692818358") == "Счет **8358"


def test_mask_from_to_one():
    assert mask_from_to("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"


def test_get_filtered_and_sorted():
    test_list = [{"state": "EXECUTED"},
                 {"date": "2019-08-26T10:50:58.294041"}]
    result = [{"state": "EXECUTED"},
              {"date": "2019-08-26T10:50:58.294041"}]

    assert get_filtered_and_sorted(test_list) == get_filtered_and_sorted(result)

def test_prepare_user_msg():
    test_list = {"id": 41428829,
                 "state": "EXECUTED",
                 "date": "2019-07-03T18:35:29.512364",
                 "operationAmount": {
                     "amount": "8221.37",
                     "currency": {
                         "name": "USD",
                         "code": "USD"
                     }
                 },
                 "description": "Перевод организации",
                 "from": "MasterCard 7158300734726758",
                 "to": "Счет 35383033474447895560"
                 }
    test_msg = """03.07.2019 Перевод организации
MasterCard 7158 30** **** 6758 -> Счет **5560
8221.37 USD"""

    assert prepare_user_msg(test_list) == test_msg
