# Написать функцию, которая получает на вход два списка чисел и возвращает новый список, содержащий
# только те числа, которые встречаются в обоих списках.


def intersection_number(list_1: list[int], list_2: list[int]) -> list[int]:
    """Функция для получения одинаковых чисел в списках"""
    # list_3 = list ()
    # for i in list_1:
    #     if i in list_2:
    #         list_3.append(i)
    # return list_3
    return [i for i in list_1 if i in list_2]


number_list = [1, 2, 3, 4], [3, 4, 5, 6]
result = intersection_number(number_list[0], number_list[1])

if __name__ == "__main__":
    print(result)
