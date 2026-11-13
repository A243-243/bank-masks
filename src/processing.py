# src/processing.py
def filter_by_state(dictionaries: list[dict], state="EXECUTED") -> list[dict]:
    """Возвращает новый список словарей по соответствующему значению ключа state."""
    filtered_list = []
    for dictionary in dictionaries:
        if dictionary['state'] == state:
            filtered_list.append(dictionary)
    return filtered_list


# Тестовые примеры
if __name__ == "__main__":
    list_of_dictionaries = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
print(filter_by_state(list_of_dictionaries, "EXECUTED"))  # Ожидаемый результат: словари со значением 'EXECUTED'
print(filter_by_state(list_of_dictionaries, "CANCELED"))  # Ожидаемый результат: словари со значением 'CANCELED'
print(filter_by_state(list_of_dictionaries)) # Ожидаемый результат без указания аргумента:
                                            # словари со значением 'EXECUTED'
