from data import UrlsData
from helpers import GenerateCourierData
import pytest
import requests


@pytest.fixture
def create_courier():
    courier_data = GenerateCourierData.generate_individual_courier_data()
    yield courier_data
    response = requests.post(f'{UrlsData.LOGIN_COURIER_ENDPOINT}', json=courier_data)
    if response.status_code == 200:
        courier_id = response.json().get('id')
        requests.delete(f'{UrlsData.DELETE_COURIER_ENDPOINT}{courier_id}')


@pytest.fixture
def create_permanent_couriers_data():
    courier = GenerateCourierData()
    return courier.generate_courier_data_permanent()


@pytest.fixture
def login_courier(create_courier):
    return create_courier
