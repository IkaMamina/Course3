from utils import get_date, mask_from_to, get_filtered_and_sorted, prepare_user_msg


def test_get_date():
    assert get_date("2019-08-26T10:50:58.294041") == "26.08.2019"


def test_mask_from_to():
    assert mask_from_to("Счет 64686473678894779589") == "Счет **9589"


def test_mask_from_to_one():
    assert mask_from_to("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"


def test_get_filtered_and_sorted():
    if "state" == "EXECUTED":
        assert get_filtered_and_sorted == ['26.08.2019 Перевод организации\n'
                                           'Maestro 1596 83** **** 5199 Счет ****9589\n'
                                           '8221.37 USD\n']


def test_prepare_user_msg():
    if "state" == "EXECUTED":
        assert prepare_user_msg == ["26.08.2019 Перевод организации\n"
                                    "Maestro 1596 83** **** 5199 -> Счет ****9589\n"
                                    "8221.37 USD\n"]
