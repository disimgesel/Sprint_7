from data import UrlsData, TextsResponseData
from conftest import create_courier, login_courier
import pytest
import allure
import requests
import helpers


@allure.suite('Позитивная авторизация курьера')
class TestPositiveLoginCourier:

    @allure.title('Успешная авторизация и наличие у курьера ID')
    def test_login_successful(self, login_courier):
        requests.post(f'{UrlsData.CREATE_COURIER_ENDPOINT}', json=login_courier)
        response = requests.post(f'{UrlsData.LOGIN_COURIER_ENDPOINT}', json=login_courier)
        assert response.status_code == 200 and response.json()["id"] is not None


@allure.suite('Негативная авторизация курьера')
class TestNegativeLoginCourier:

    @allure.title('Не авторизация курьера с незаполнным обязательным полем')
    @pytest.mark.parametrize('key, value', [('login', ''), ('password', '')])
    def test_can_not_auth_with_incomplete_data(self, create_courier, key, value):
        create_courier[key] = value
        response = requests.post(f'{UrlsData.LOGIN_COURIER_ENDPOINT}', json=create_courier)
        assert response.status_code == 400 and response.text == TextsResponseData.ERROR_NOT_ENOUGH_DATA_FOR_LOGIN

    @allure.title('Не авторизация курьера с не существующим логином в базе созданных пользователей')
    @pytest.mark.parametrize('key, value', [('login', helpers.GenerateCourierData.generate_individual_courier_data()), ('password', helpers.GenerateCourierData.generate_individual_courier_data())])
    def test_can_not_auth_login_not_found(self, create_courier, key, value):
        requests.post(f'{UrlsData.CREATE_COURIER_ENDPOINT}', json=create_courier)
        create_courier[key] = value
        response = requests.post(f'{UrlsData.LOGIN_COURIER_ENDPOINT}', data=create_courier)
        assert response.status_code == 404 and response.text == TextsResponseData.ERROR_ACCOUNT_NOT_FOUND
