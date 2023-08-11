from utils import load_5_operations_from_json, normalizing_date, censor_card, censor_bank


file = "../operations.json"


def main():
    operations = load_5_operations_from_json(file)
    for operation in operations:
        operation['date'] = normalizing_date(operation['date'])

        try:
            if "Счет" in operation['from']:
                operation['from'] = censor_card(operation['from'])
            else:
                operation['from'] = censor_card(operation['from'])
        except LookupError:
            operation['from'] = "Непонятный формат"

        if "Счет" in operation['to']:
            operation['to'] = censor_bank(operation['to'])
        else:
            operation['to'] = censor_bank(operation['to'])

        print(f"""
{operation['date']} {operation['description']}
{operation['from']} -> {operation['to']}
{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}""")


if __name__ == '__main__':
    main()



