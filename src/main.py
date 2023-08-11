import json

def load_json_on_python(file):
    """
    берем json файл и выбираем 5 последних операций
    """
    with open(file, 'r', encoding='utf-8') as f:
        loaded = json.load(f)
        list_for_json = []
        for operation in loaded:
            try:
                if operation['state'] == 'EXECUTED':
                    list_for_json.append(operation)

            except LookupError:
                error = "ОШИБКА!!"
        sort_operations = sorted(list_for_json, key=lambda x: x["date"], reverse=True)
        last_operations = sort_operations[:5]

        return last_operations




def normalizing_date(data):
    """
    делаем приемлимую дату не как в json файле
    """
    formated_date = data[8:10] + '.' + data[5:7] + '.' + data[:4]
    return formated_date


def censor_card_number(card_number):
    """
    получаем номер карты и цензурим его
    """
    old_card = card_number.split(' ')
    new_card = old_card[-1][:4] + ' ' + old_card[-1][4:6] + '**' + ' ' + '****' + ' ' + old_card[-1][-4:]
    old_card[-1] = new_card
    return " ".join(old_card)


def censor_bank_number(bank_number):
    """
    получаем номер счета и цензурим
    """
    old_number = bank_number.split(" ")
    new_number = '**' + old_number[-1][-4:]
    old_number[-1] = new_number
    return " ".join(old_number)

