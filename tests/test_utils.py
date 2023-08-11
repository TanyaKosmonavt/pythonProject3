from src.utils import load_5_operations_from_json, normalizing_date, censor_card, censor_bank

test_file = "tests/for_testing_utils.json"

def test_normalizing_date():
    assert normalizing_date("2017-08-26T10:50:58.294041") == "26.08.2017"
    assert normalizing_date("2017-03-23T10:45:06.972075") == "23.03.2017"
    assert normalizing_date("2020-08-26T10:50:58") == "26.08.2020"
    assert normalizing_date("2020-11-05") == "05.11.2020"


def test_censor_card():
    assert censor_card("Visa Gold 7756673469642765") == "Visa Gold 7756 67** **** 2765"
    assert censor_card("Maestro 7810846596785552") == "Maestro 7810 84** **** 5552"
    assert censor_card("МИР 1582474475540985") == "МИР 1582 47** **** 0985"


def test_censor_bank():
    assert censor_bank("Счет 12189246980267075657") == "Счет **5657"
    assert censor_bank("Счет 95473010446151855505") == "Счет **5505"
    assert censor_bank("Счет 15574304810835774222") == "Счет **4222"


def test_load_5_operations_from_json():
    from_file = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        }
    ]
    assert load_5_operations_from_json(test_file) == from_file