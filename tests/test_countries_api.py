import pytest
from clients.countries_client import CountriesClient

@pytest.mark.parametrize(
    "country_name",
    ["United Kingdom", "Germany", "Japan"]
)
def test_get_country_by_name(country_name):
    response = CountriesClient.get_country_by_name(country_name)

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert data[0]["name"]["common"] == country_name


@pytest.mark.parametrize(
    "country_code",
    ["GB", "DE", "JP"]
)
def test_get_country_by_code(country_code):
    response = CountriesClient.get_country_by_code(country_code)

    assert response.status_code == 200

    data = response.json()
    assert data[0]["cca2"] == country_code


def test_get_country_with_invalid_name():
    response = CountriesClient.get_country_by_name("InvalidCountry123")

    assert response.status_code in [400, 404]

def test_get_country_with_invalid_code():
    response = CountriesClient.get_country_by_code("UK")

    assert response.status_code in [400, 404]

