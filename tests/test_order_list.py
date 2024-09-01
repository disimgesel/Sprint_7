from data import UrlsData
import requests
import allure


@allure.suite('Получение списка заказов')
class TestOrderList:

    @allure.title('Получение списка заказов и возвращение тела ответа')
    def test_get_orders_list(self):
        response = requests.get(f'{UrlsData.ORDER_LIST_ENDPOINT}')
        assert response.status_code == 200 and 'orders' in response.json()
