import pytest


@pytest.fixture
def transactions() -> list[dict]:
    """Список словарей с разными комбинациями state и date."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 3, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 4, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 5, "state": "PENDING", "date": "2020-01-15T10:00:00.000000"},
    ]


@pytest.fixture
def transactions_same_dates() -> list[dict]:
    """Словари с одинаковыми датами — для проверки стабильности сортировки."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2020-01-01T00:00:00"},
        {"id": 2, "state": "EXECUTED", "date": "2020-01-01T00:00:00"},
        {"id": 3, "state": "CANCELED", "date": "2020-01-01T00:00:00"},
    ]


@pytest.fixture
def empty_transactions() -> list[dict]:
    """Пустой список — граничный случай."""
    return []
