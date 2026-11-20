import pytest

from src.masks import get_mask_account, get_mask_card_number


class TestGetMaskCardNumber:
    @pytest.mark.parametrize(
        "card_number, expected",
        [
            ("7000792289606361", "7000 79** **** 6361"),
            ("1234567812345678", "1234 56** **** 5678"),
            ("11112222333344445555", "1111 22** **** 4444 5555"),  # 20 цифр
            ("9876543210987654321", "9876 54** **** 7654 321"),  # 19 цифр
            ("123456789012", "1234 56** ****"),  # минимальная длина 12
        ],
    )
    def test_masks_card_number_correctly(self, card_number, expected):
        assert get_mask_card_number(card_number) == expected

    @pytest.mark.parametrize("card_number", ["1234", "", "12345678901"])
    def test_too_short_number_raises_index_error(self, card_number):
        with pytest.raises(IndexError):
            get_mask_card_number(card_number)


class TestGetMaskAccount:
    @pytest.mark.parametrize(
        "account_number, expected",
        [
            ("73654108430135874305", "**4305"),  # 20 цифр
            ("40817810000000000001", "**0001"),  # 20 цифр
            ("1234567890123456", "**"),  # 16 цифр — минимальная рабочая длина
            ("12345678901234567890", "**7890"),  # 20 цифр, другой хвост
        ],
    )
    def test_masks_account_correctly(self, account_number, expected):
        assert get_mask_account(account_number) == expected

    @pytest.mark.parametrize(
        "account_number", ["", "123", "1234567890", "12345678901234", "123456789012345"]
    )
    def test_too_short_account_raises_index_error(self, account_number):
        with pytest.raises(IndexError):
            get_mask_account(account_number)