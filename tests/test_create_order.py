from data import OrderData, UrlsData
import pytest
import requests
import allure


@allure.suite('Создание заказа')
class TestCreateOrder:

    @allure.title('Создание заказа с выбором цвета и вхождением track в тело ответа')
    @pytest.mark.parametrize('color', OrderData.scooter_color)
    def test_choice_scooter_color(self, color):
        order_data = OrderData.order_data
        order_data['color'] = color
        response = requests.post(f'{UrlsData.CREATE_ORDER_ENDPOINT}', json=order_data)
        assert response.status_code == 201 and 'track' in response.text
