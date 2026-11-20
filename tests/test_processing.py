import pytest

from src.processing import filter_by_state, sort_by_date


class TestFilterByState:
    def test_default_state_is_executed(self, transactions):
        result = filter_by_state(transactions)
        assert all(item["state"] == "EXECUTED" for item in result)
        assert len(result) == 2

    @pytest.mark.parametrize("state", ["EXECUTED", "CANCELED", "PENDING"])
    def test_filtering_by_state(self, transactions, state):
        result = filter_by_state(transactions, state)
        assert all(item["state"] == state for item in result)

    def test_absent_state_returns_empty_list(self, transactions):
        assert filter_by_state(transactions, "UNKNOWN") == []

    def test_empty_list_returns_empty_list(self, empty_transactions):
        assert filter_by_state(empty_transactions) == []


class TestSortByDate:
    def test_sort_descending_by_default(self, transactions):
        result = sort_by_date(transactions)
        dates = [item["date"] for item in result]
        assert dates == sorted(dates, reverse=True)

    def test_sort_ascending(self, transactions):
        result = sort_by_date(transactions, reverse=False)
        dates = [item["date"] for item in result]
        assert dates == sorted(dates)

    def test_equal_dates_keep_original_order(self, transactions_same_dates):
        result = sort_by_date(transactions_same_dates, reverse=True)
        assert [item["id"] for item in result] == [1, 2, 3]

    def test_missing_date_key_raises_key_error(self, transactions):
        broken = [{"id": 9, "state": "EXECUTED"}] + transactions
        with pytest.raises(KeyError):
            sort_by_date(broken)