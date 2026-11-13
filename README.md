# Widget банковских операций клиента

## Цель проекта

Проект для обработки данных о банковских операциях клиента: маскировка
реквизитов карт и счетов, фильтрация и сортировка операций.

## Установка

1. Клонируйте репозиторий:
   git clone https://github.com/A243-243/bank-masks.git
2. Установите зависимости (проект использует Poetry):
   poetry install

## Использование

Модуль src/processing содержит функции обработки данных:

- filter_by_state(transactions, state='EXECUTED') — возвращает новый список
  словарей, отфильтрованный по значению ключа state;
- sort_by_date(transactions, reverse=True) — возвращает новый список словарей,
  отсортированный по дате (по умолчанию — от последней к первой).

## Пример работы

```python
from src.processing import filter_by_state, sort_by_date

transactions = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
]

filter_by_state(transactions)
# [{'id': 41428829, ...}, {'id': 939719570, ...}]

sort_by_date(transactions)
# [{'id': 41428829, ...}, {'id': 594226727, ...}, {'id': 939719570, ...}]
text
