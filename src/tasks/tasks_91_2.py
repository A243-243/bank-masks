# Написать функцию, которая получает на вход список чисел и возвращает новый список,
# содержащий только числа, которые являются палиндромами.


def palindrome_number(list: list[int]) -> list[int]:
    """Функция для получения чисел, которые являются палиндромами"""
    # list_2 = []
    # for i in number_list:
    #     if str(i) == str(i)[::-1]:
    #         list_2.append(i)
    # return list_2
    return [i for i in number_list if str(i) == str(i)[::-1]]


number_list = [121, 123, 131, 34543]
result = palindrome_number(number_list)

if __name__ == "__main__":
    print(result)
