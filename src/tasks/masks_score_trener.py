# src/masks.py
def get_mask_account(text: int) -> str:
    """Заменяет символы текста на указанный символ и скрывает группы символов."""

    score_number = str(73654108430135874305)
    chars = list(score_number)  # Превращает строку в список, разделяя на отдельные символы
    for i in range(14, 16):  # Заменяет числа в списке на звездочку, по срезу [14:16]
        chars[i] = "*"
    new_chars = chars[14 : len(chars)]  # Забирает из списка последние шесть элементов по срезу [14:len(chars)]
    result = "".join(new_chars)
    return result


score_number = 73654108430135874305
mask_score = get_mask_account(score_number)
print(mask_score)  # Выводит результат работы функции
