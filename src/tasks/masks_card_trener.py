# src/masks.py
def get_mask_card_number(text: int) -> str:
    """Заменяет символы текста на указанный символ и группирует символы."""

    card_number = str(7000792289606361)
    chars = list(card_number)  # Превращает строку в список, разделяя на отдельные символы
    for i in range(6, 12):  # Заменяет числа в списке на звездочку, по срезу [6:12]
        chars[i] = "*"
        result = " ".join(
            ["".join(chars[i : i + 4]) for i in range(0, len(chars), 4)]
        )  # Собирает в группы по 4 символа
    return result


card_number = 7000792289606361
mask_card = get_mask_card_number(card_number)
print(mask_card)  # Выводит результат работы функции
