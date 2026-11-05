from pathlib import Path

def clear_names(file_name: str) -> list:
    """ Функция для очистки имен от лишних символов"""
    new_names_list = list()
    # путь от корня проекта до файла data/names.txt
    file_path = Path(__file__).parents[2] / 'data' / file_name
    with file_path.open('r', encoding='utf-8') as names_file:
        # names_list = names_file.readlines()
        names_list = names_file.read().split()
        for name in names_list:
            new_name = ''
            for symbol in name:
                if symbol.isalpha():
                    new_name = new_name + symbol
            if new_name.isalpha():
                new_names_list.append(new_name)
    return new_names_list


if __name__ == '__main__':
    cleared_name = clear_names('names.txt')

    for i in cleared_name:
        print(i)
