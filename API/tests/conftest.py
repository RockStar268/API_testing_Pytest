import pytest


@pytest.fixture()
def base_url():
    return "https://latest-stock-price.p.rapidapi.com/"


@pytest.fixture()
def header():
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "0f706f2146msh8c56e8e2a6f8bd5p12678djsn9cc14bf4eddd",
        "X-RapidAPI-Host": "latest-stock-price.p.rapidapi.com"
    }
    return headers

