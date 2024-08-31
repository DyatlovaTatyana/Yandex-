import pytest
import requests


def test_case1(base_url_org, base_url_geocod, api_key_org):
#запрос по 5 ближайшим кафе
    query_params_org = {
    "apikey": api_key_org,
    "text": "кафе",
    "lang": "ru_RU",
    "ll": "30.360909,59.931058",
    "spn": "0.01,0.01",
    "type": "biz",
    "results":"5"
    }

    response2 = requests.get(base_url_org, params=query_params_org)
    print(response2.status_code)
    print("Поиск ближайших кафе" + response2.text)
    assert response2.status_code == 200
    info1 = response2.json()
    uri_find = info1["features"][0]["properties"]["uri"]

#запрос по uri кафе из прошлого запроса
    query_params_cafe = {
    "apikey":"a796ba84-f8b6-4da5-816d-cdf84abe973f",
    "format": "json",
    "uri": uri_find
    }

    response3 = requests.get(base_url_geocod, params=query_params_cafe)
    print(response3.status_code)
    print("Поиск по uri кафе" + response3.text)
    assert response3.status_code == 200
    info = response3.json()
    assert info["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["name"] == "Забыли сахар"

def test_case2(base_url_org):
# проверка ответа при пустом АПИ ключе
    query_params_org = {
    "apikey": " ",
    "text": "кафе",
    "lang": "ru_RU",
    "ll": "30.360909,59.931058",
    "spn": "0.01,0.01",
    "type": "biz",
    "results":"5"
    }

    response4 = requests.get(base_url_org, params=query_params_org)
    print(response4.status_code)
    print("Поиск ближайших кафе" + response4.text)
    assert response4.status_code == 403
    info = response4.json()
    assert info["message"] == "Invalid api key"

@pytest.mark.parametrize("test_data", ["a796ba84-f8b6-4da5-816d-cdf84abe973f", "3955de07-1c77-458e-9f5a-6ead5d5dc5b3", " "])
def test_case3(base_url_org, test_data):
#проверка через марку разных вариантов ключей (верный, неверный, пустой)
    query_params_org = {
    "apikey": test_data,
    "text": "кафе",
    "lang": "ru_RU",
    "ll": "30.360909,59.931058",
    "spn": "0.01,0.01",
    "type": "biz",
    "results":"5"
    }

    response5 = requests.get(base_url_org, params=query_params_org)
    assert test_data == "3955de07-1c77-458e-9f5a-6ead5d5dc5b3"