import pytest
import requests

@pytest.fixture(scope="module")
def base_url_geocod():
    base_url_geocod = "https://geocode-maps.yandex.ru/1.x/"
    return base_url_geocod

@pytest.fixture(scope="module")
def base_url_org():
    base_url_org = "https://search-maps.yandex.ru/v1/"
    return base_url_org

@pytest.fixture(scope="module")
def api_key_geocod():
    api_key_geocod = "a796ba84-f8b6-4da5-816d-cdf84abe973f"
    return api_key_geocod

@pytest.fixture(scope="module")
def api_key_org():
    api_key_org = "3955de07-1c77-458e-9f5a-6ead5d5dc5b3"
    return api_key_org


#setup
@pytest.fixture(scope="module", autouse=True)
def setup(base_url_geocod, api_key_geocod):
    # запрос по адресу
    query_params_geocod = {
        "apikey": api_key_geocod,
        "geocode": "Невский проспект дом 1",
        "format": "json"
    }

    response = requests.get(base_url_geocod, params=query_params_geocod)
    print(response.status_code)
    print("Поиск по геокоду" + response.text)
    assert response.status_code == 200

