import pytest
import requests

from API.resources.enums.status import Status
from API.resources.enums.error_messages import ErrorMessages


@pytest.mark.parametrize("indices", [
    "NIFTY 50",
    "NIFTY NEXT 50",
    "NIFTY BANK"
])
def test_get_price(base_url, header, indices):
    querystring = {
        "Indices": indices
    }

    url = base_url + "price"
    response = requests.get(url, headers=header, params=querystring)

    assert response.status_code == Status.SUCCESS.value
    assert response.json()[0].get("symbol") == indices


@pytest.mark.parametrize("indices", [
    "BANDHANBNK",
    "NIFT BANK"
])
@pytest.mark.xfail(raises=IndexError)
def test_get_price_invalid_input(base_url, header, indices):
    querystring = {
        "Indices": indices
    }

    url = base_url + "price"
    response = requests.get(url, headers=header, params=querystring)
    print(response.json())
    assert response.status_code == Status.SUCCESS.value
    assert response.json()[0].get("symbol") == indices


@pytest.mark.parametrize("indices", [""])
@pytest.mark.regression
def test_get_prices_empty_indices(base_url, header, indices):
    querystring = {
        "Indices": indices
    }

    url = base_url + "price"
    response = requests.get(url, headers=header, params=querystring)

    assert response.status_code == Status.BAD_REQUEST.value
    assert response.json().get("error") == ErrorMessages.CHAR_LENGTH.value
    assert response.json().get("error_code") == ErrorMessages.INVALID_PARAMETER.value


