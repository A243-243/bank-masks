import pytest

from src.widget import get_date, get_user_input, mask_account_card


class TestMaskAccountCard:
    @pytest.mark.parametrize(
        "input_data, expected",
        [
            ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
            ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
            ("Счет 73654108430135874305", "Счет **4305"),
            ("Счёт 73654108430135874305", "Счёт **4305"),
        ],
    )
    def test_masks_card_and_account(self, input_data, expected):
        assert mask_account_card(input_data) == expected

    def test_latin_name_gets_card_mask(self):
        """Функция выбирает маску по наличию кириллицы: латиница → маска карты."""
        assert (
            mask_account_card("Account 73654108430135874305")
            == "Account 7365 41** **** 3587 4305"
        )

    @pytest.mark.parametrize("bad_input", ["", "   "])
    def test_empty_input_raises_index_error(self, bad_input):
        with pytest.raises(IndexError):
            mask_account_card(bad_input)

    def test_none_raises_type_error(self):
        with pytest.raises(TypeError):
            mask_account_card(None)


class TestGetDate:
    @pytest.mark.parametrize(
        "date_str, expected",
        [
            ("2024-03-11T02:26:18.671407", "11.03.2024"),
            ("2019-07-03T18:35:29.512364", "03.07.2019"),
            ("2018-06-30", "30.06.2018"),  # дата без времени тоже валидна
        ],
    )
    def test_converts_date(self, date_str, expected):
        assert get_date(date_str) == expected

    @pytest.mark.parametrize("bad_date", ["", "invalid", "2024-13-01T00:00:00"])
    def test_invalid_date_raises_value_error(self, bad_date):
        with pytest.raises(ValueError):
            get_date(bad_date)

    def test_none_raises_type_error(self):
        with pytest.raises(TypeError):
            get_date(None)


class TestGetUserInput:
    def test_valid_input(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "Visa Platinum 7000792289606361")
        assert get_user_input() == "Visa Platinum 7000792289606361"

    def test_invalid_then_valid_input(self, monkeypatch):
        answers = iter(
            [
                "",  # пустой ввод
                "a b c d",  # больше трёх подстрок
                "a  b  c",  # больше двух пробелов
                "Сч",  # слишком короткая строка
                "Счёт 73654108430135874305",  # валидный ввод
            ]
        )
        monkeypatch.setattr("builtins.input", lambda _: next(answers))
        assert get_user_input() == "Счёт 73654108430135874305"