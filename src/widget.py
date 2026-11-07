import re
from datetime import datetime
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


def get_date(date: str) -> str:
    """Переводит дату в формат ДД.ММ.ГГГГ"""
    date_form = datetime.fromisoformat(date)
    return date_form.strftime("%d.%m.%Y")



if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Maestro 7000792289606361"))
    print(mask_account_card("Счет 73654108430135874305"))
    print(get_date("2024-03-11T02:26:18.671407"))