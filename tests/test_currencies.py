from decimal import Decimal

import pytest
from pycountries.currencies import (
    AmountSpecialValuesNotAllowedError,
    Currency,
    NegativeAmountNotAllowedError,
    WrongAmountDigitsNumberError,
    WrongAmountTypeError,
    ZeroAmountNotAllowedError,
)


class TestCurrencyCleanAmount:
    two_digits_currency = Currency.two_digits[0]

    def test_clean_amount_should_raise_amount_special_values_not_allowed_error_when_currency_has_two_digits_and_amount_is_inf_decimal(  # noqa: E501
        self,
    ):
        amount: Decimal = Decimal("inf")
        with pytest.raises(AmountSpecialValuesNotAllowedError):
            self.two_digits_currency.clean_amount(amount)

    def test_clean_amount_should_raise_negative_amount_not_allowed_error_when_currency_has_two_digits_and_amount_is_negative_decimal(  # noqa: E501
        self,
    ):
        amount: Decimal = Decimal("-20")
        with pytest.raises(NegativeAmountNotAllowedError):
            self.two_digits_currency.clean_amount(amount)

    def test_clean_amount_should_raise_wrong_amount_digits_number_error_when_currency_has_two_digits_and_amount_is_decimal_and_has_three_digits(  # noqa: E501
        self,
    ):
        amount: Decimal = Decimal("1.234")
        with pytest.raises(WrongAmountDigitsNumberError):
            self.two_digits_currency.clean_amount(amount)

    def test_clean_amount_should_raise_wrong_amount_type_error_when_currency_has_two_digits_and_amount_is_int(self):
        amount: int = 1
        with pytest.raises(WrongAmountTypeError):
            self.two_digits_currency.clean_amount(amount)

    def test_clean_amount_should_raise_zero_amount_not_allowed_error_when_amount_is_zero_decimal_and_allow_zero_is_false(  # noqa: E501
        self,
    ):
        amount: Decimal = Decimal("0")
        with pytest.raises(ZeroAmountNotAllowedError):
            self.two_digits_currency.clean_amount(amount, allow_zero=False)

    def test_clean_amount_should_return_zero_decimal_when_amount_is_zero_decimal_and_allow_zero_is_true(self):
        amount: Decimal = Decimal("0")
        assert self.two_digits_currency.clean_amount(amount) == amount

    def test_clean_amount_should_return_fixed_digest_decimal_when_currency_has_two_digits_and_amount_has_missing_digits(
        self,
    ):
        amount: Decimal = Decimal("20.2")
        assert str(self.two_digits_currency.clean_amount(amount)) == str(Decimal("20.20"))


class TestCurrencyGetByValue:
    def test_get_by_value_should_return_currency_usd_when_value_is_alpha_3_usd(self):
        assert Currency("USD") == Currency.USD

    def test_get_by_value_should_return_currency_usd_when_value_is_numeric_str_840(self):
        assert Currency("840") == Currency.USD

    def test_get_by_value_should_return_currency_usd_when_value_is_numeric_int_840(self):
        assert Currency(840) == Currency.USD

    def test_get_by_value_should_return_currency_all_when_value_is_numeric_str_008(self):
        assert Currency("008") == Currency.ALL

    def test_get_by_value_should_return_currency_all_when_value_is_numeric_int_8(self):
        assert Currency(8) == Currency.ALL
