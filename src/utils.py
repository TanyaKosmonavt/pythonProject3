import json

def load_5_operations_from_json(file):
    """
    загружаем джсон файл и делаем выборку первых 5 словарей
    """
    with open(file, 'r', encoding='utf-8') as f:
        loaded = json.load(f)
        operation_list = []
        for operation in loaded:
            try:
                if operation['state'] == 'EXECUTED':
                    operation_list.append(operation)
            except LookupError:
                error = "ОШИБКА!"
        sorted_operations = sorted(operation_list, key=lambda x: x["date"], reverse=True)
        last_operations = sorted_operations[:5]

        return last_operations


def normalizing_date(data):
    """
    берем дату ,которая была в джсон файле и конвертируем в приемлимую для нас
    """
    normal_date = data[8:10] + '.' + data[5:7] + '.' + data[:4]
    return normal_date

def censor_card(card_number):
    """
    получаем номер карты и цензурим его звездочками
    """
    old_card = card_number.split(' ')
    new_card = old_card[-1][:4] + ' ' + old_card[-1][4:6] + '**' + ' ' + '****' + ' ' + old_card[-1][-4:]
    old_card[-1] = new_card
    return " ".join(old_card)


def censor_bank(bank_number):
    """
    получаем номер счета и цензурим его звездочками
    """
    old_number = bank_number.split(" ")
    new_number = '**' + old_number[-1][-4:]
    old_number[-1] = new_number
    return " ".join(old_number)