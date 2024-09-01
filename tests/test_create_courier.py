from data import UrlsData, TextsResponseData
from conftest import create_courier
from conftest import create_permanent_couriers_data
import pytest
import allure
import requests


@allure.suite('Позитивное создание курьера')
class TestPositiveCreateCourier:

    @allure.title('Успешное создание курьера с всеми заполненными полями валидными значениями')
    def test_create_new_courier_with_valid_full_data(self, create_courier):
        response = requests.post(f'{UrlsData.CREATE_COURIER_ENDPOINT}', json=create_courier)
        assert response.status_code == 201 and response.text == TextsResponseData.SUCCESSFUL_CREATE_COURIER


@allure.suite('Негативное создание курьера')
class TestNegativeCreateCourier:

    @allure.title('Не создание курьера с логином, который имеется у уже созданного пользователя')
    def test_can_not_create_new_courier_with_identical_login(self, create_permanent_couriers_data):
        requests.post(f'{UrlsData.CREATE_COURIER_ENDPOINT}', json=create_permanent_couriers_data)
        response = requests.post(f'{UrlsData.CREATE_COURIER_ENDPOINT}', json=create_permanent_couriers_data)
        assert response.status_code == 409 and response.text == TextsResponseData.ERROR_LOGIN_ALREADY_USED

    @allure.title('Не создание курьера с одним не заполненным обязательным полем')
    @pytest.mark.parametrize('key, value', [('login', ''), ('password', '')])
    def test_can_not_create_new_courier_with_incomplete_data(self, create_courier, key, value):
        create_courier[key] = value
        response = requests.post(f'{UrlsData.CREATE_COURIER_ENDPOINT}', json=create_courier)
        assert response.status_code == 400 and response.text == TextsResponseData.ERROR_NOT_ENOUGH_DATA
