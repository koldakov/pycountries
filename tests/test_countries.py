from pycountries.countries import Country


class TestCountryGetByValue:
    def test_get_by_value_should_return_country_usa_when_value_is_alpha_2_us(self):
        assert Country("US") == Country.US

    def test_get_by_value_should_return_country_usa_when_value_is_alpha_3_usa(self):
        assert Country("USA") == Country.US

    def test_get_by_value_should_return_country_usa_when_value_is_numeric_str_840(self):
        assert Country("840") == Country.US

    def test_get_by_value_should_return_country_usa_when_value_is_numeric_int_840(self):
        assert Country(840) == Country.US

    def test_get_by_value_should_return_country_afg_when_value_is_numeric_str_004(self):
        assert Country("004") == Country.AF

    def test_get_by_value_should_return_country_afg_when_value_is_numeric_int_4(self):
        assert Country(4) == Country.AF
