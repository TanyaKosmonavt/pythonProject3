from src.utils import load_5_operations_from_json, normalizing_date, censor_card, censor_bank

test_file = "for_testing_utils.json"

def test_normalizing_date():
    assert normalizing_date("2017-08-26T10:50:58.294041") == "26.08.2017"
    assert normalizing_date("2017-03-23T10:45:06.972075") == "23.03.2017"
    assert normalizing_date("2020-08-26T10:50:58") == "26.08.2020"
    assert normalizing_date("2020-11-05") == "05.11.2020"


def test_censor_card():
    assert censor_card("Visa Gold 7756673469642839") == "Visa Gold 7756 67** **** 2839"
    assert censor_card("Maestro 7810846596785568") == "Maestro 7810 84** **** 5568"
    assert censor_card("МИР 1582474475547301") == "МИР 1582 47** **** 7301"


def test_censor_bank():
    assert censor_bank("Счет 12189246980267075758") == "Счет **5758"
    assert censor_bank("Счет 95473010446151855633") == "Счет **5633"
    assert censor_bank("Счет 15574304810835774010") == "Счет **4010"


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