# Написать функцию, которая получает на вход два списка чисел и возвращает новый список,
# содержащий только те числа, которые есть только в одном из списков.


def unique_number(list_1: list[int], list_2: list[int]) -> list[int]:
    """Функция для получения чисел, которые есть только в одном из списков"""
    # вариант 1
    # list_3 = list ()
    # for i in list_1:
    #     if i not in list_2:
    #         list_3.append(i)
    # for i in list_2:
    #     if i not in list_1:
    #         list_3.append(i)
    # return list_3

    # вариант 2
    # return [i for i in list_1 if i not in list_2] + [i for i in list_2 if i not in list_1]

    # вариант 3 через множества (пока не оптимально)
    return list(set(list_1) - set(list_2)) + list(set(list_2) - set(list_1))

    # вариант 4 через множества (быстро и лаконично). Здесь ^ это «симметрическая разность».
    # return list(set(list_1) ^ set(list_2))


number_list = [1, 2, 3, 4], [3, 4, 5, 6]
result = unique_number(number_list[0], number_list[1])

if __name__ == "__main__":
    print(result)
