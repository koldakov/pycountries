import pytest
from pycountries.macro_languages import MacroLanguage


class TestMacroLanguageGetByValue:
    def test_get_by_value_should_raise_value_error_when_value_is_non_existent_i_id(self):
        with pytest.raises(ValueError):
            MacroLanguage("non_existent")
