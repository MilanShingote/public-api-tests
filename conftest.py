import pytest
from clients.countries_client import CountriesClient


@pytest.fixture
def countries_client():
    return CountriesClient()
