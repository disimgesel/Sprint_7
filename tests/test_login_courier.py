from data import UrlsData, TextsResponseData
from conftest import create_individual_courier_data
import pytest
import allure
import requests
import helpers


@allure.suite('Позитивная авторизация курьера')
class TestPositiveLoginCourier:

    @allure.title('Успешная авторизация и наличие у курьера ID')
    def test_login_successful(self, create_individual_courier_data):
        requests.post(f'{UrlsData.CREATE_COURIER_ENDPOINT}', json=create_individual_courier_data)
        response = requests.post(f'{UrlsData.LOGIN_COURIER_ENDPOINT}', json=create_individual_courier_data)
        assert response.status_code == 200 and response.json()["id"] is not None
        courier_id = response.json().get('id')
        requests.delete(f'{UrlsData.DELETE_COURIER_ENDPOINT}{courier_id}')


@allure.suite('Негативная авторизация курьера')
class TestNegativeLoginCourier:

    @allure.title('Не авторизация курьера с незаполнным обязательным полем')
    @pytest.mark.parametrize('key, value', [('login', ''), ('password', '')])
    def test_can_not_auth_with_incomplete_data(self, create_individual_courier_data, key, value):
        create_individual_courier_data[key] = value
        response = requests.post(f'{UrlsData.LOGIN_COURIER_ENDPOINT}', json=create_individual_courier_data)
        assert response.status_code == 400 and response.text == TextsResponseData.ERROR_NOT_ENOUGH_DATA_FOR_LOGIN

    @allure.title('Не авторизация курьера с не существующим логином в базе созданных пользователей')
    @pytest.mark.parametrize('key, value', [('login', helpers.GenerateCourierData.generate_individual_courier_data()), ('password', helpers.GenerateCourierData.generate_individual_courier_data())])
    def test_can_not_auth_login_not_found(self, create_individual_courier_data, key, value):
        requests.post(f'{UrlsData.CREATE_COURIER_ENDPOINT}', json=create_individual_courier_data)
        create_individual_courier_data[key] = value
        response = requests.post(f'{UrlsData.LOGIN_COURIER_ENDPOINT}', data=create_individual_courier_data)
        assert response.status_code == 404 and response.text == TextsResponseData.ERROR_ACCOUNT_NOT_FOUND
