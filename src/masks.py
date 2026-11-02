# src/masks.py
def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты в формате XXXX XX** **** XXXX."""

    chars = list(card_number)  # Преобразует входную строку в список, разделяя на отдельные символы.
    for i in range(6, 12):  # Маскирует символы с 6 по 11 включительно, заменяя число на звездочку, по срезу [6:12].
        chars[i] = "*"
    result = " ".join(
        ["".join(chars[i : i + 4]) for i in range(0, len(chars), 4)]
    )  # Собирает результат в группы по 4 символа с пробелами.
    return result


def get_mask_account(account_number: str) -> str:
    """Маскирует номер банковского счета в формате **XXXX."""

    chars = list(account_number)  # Преобразует входную строку в список, разделяя на отдельные символы.
    for i in range(14, 16):  # Маскирует символы с 14 по 15 включительно, заменяя число на звездочку, по срезу [14:16]
        chars[i] = "*"
    new_chars = chars[14 : len(chars)]  # Забирает из списка последние шесть символов строки по срезу [14:len(chars)]
    result = "".join(new_chars)
    return result


# Тестовые примеры
if __name__ == "__main__":
    card_number = "7000792289606361"
    print(get_mask_card_number(card_number))  # Ожидаемый результат: 7000 79** **** 6361

    account_number = "73654108430135874305"
    print(get_mask_account(account_number))  # Ожидаемый результат: **4305
