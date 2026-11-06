"""Модуль main.py — точка входа в приложение.

Предназначен для запуска и демонстрации работы функций маскирования
банковских данных из модуля src.masks:
- get_mask_card_number — маскирует номер карты по шаблону XXXX XX** **** XXXX;
- get_mask_account — маскирует номер счета по шаблону **XXXX.

В текущем виде содержит тестовые примеры с фиксированными данными.
В будущем может быть расширен для обработки пользовательского ввода.
"""
from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card

def main():
    """Запускает демонстрацию работы функций маскирования банковских данных.

        Выполняет тестирование:
        - маскирует номер карты через get_mask_card_number;
        - маскирует номер счета через get_mask_account.

        Выводит результаты в консоль в формате: «Исходное значение → Результат».
        """
    # Тестирование маскирования карты
    card_number = "7000792289606361"
    masked_card = get_mask_card_number(card_number)
    print(f"Карта: {card_number} → {masked_card}")

    # Тестирование маскирования счета
    account_number = "73654108430135874305"
    masked_account = get_mask_account(account_number)
    print(f"Счет: {account_number} → {masked_account}")

    # Тестирование определения типа счет/карта
    account_or_card_number = "MasterCard 7158300734726758"
    of_card_or_account_type = mask_account_card(account_or_card_number)
    print(f"Тип: {account_or_card_number} → {of_card_or_account_type}")



if __name__ == "__main__":
    main()
