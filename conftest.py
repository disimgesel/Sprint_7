from helpers import GenerateCourierData
import pytest


@pytest.fixture
def create_individual_courier_data():
    courier_data = GenerateCourierData.generate_individual_courier_data()
    yield courier_data


@pytest.fixture
def create_permanent_couriers_data():
    courier = GenerateCourierData()
    return courier.generate_courier_data_permanent()
