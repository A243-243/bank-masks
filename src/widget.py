import re
from src.masks import get_mask_account, get_mask_card_number

# src/widget.py
def mask_account_card(account_card: str) -> str:
    """Обрабатывает номер банковского счета и карты для дальнейшей корректной маскировки."""
    name = ""
    number = ""
    for symbol in account_card:
        if symbol.isalpha() or symbol == " ":  # буквы и пробелы — это имя
            name += symbol
        elif symbol.isdigit():  # цифры — это номер
            number += symbol
    name = name.strip()  # убираем пробелы по краям

    mask_func = get_mask_account if re.search("[а-яА-Я]", name) else get_mask_card_number
    return f"{name} {mask_func(number)}"

if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Maestro 7000792289606361"))
    print(mask_account_card("Счет 73654108430135874305"))