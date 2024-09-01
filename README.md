# QA_python_7
Проект содержит UI тесты для web-сервиса "Яндекс.Самокат", URL = https://qa-scooter.praktikum-services.ru
В директории tests находятся файлы с тестами:
    - test_create_courier:
        - def test_create_new_courier_with_valid_full_data (Успешное создание курьера с всеми заполненными полями валидными значениями)
        - def test_can_not_create_new_courier_with_identical_login (Не создание курьера с логином, который имеется у уже созданного пользователя) 
        - def test_can_not_create_new_courier_with_incomplete_data (Не создание курьера с одним не заполненным обязательным полем)
    - test_create_order:
        - def test_choice_scooter_color (Создание заказа с выбором цвета и вхождением track в тело ответа)
    - test_login_courier:
        - def test_login_successful (Успешная авторизация и наличие у курьера ID)
        - def test_can_not_auth_with_incomplete_data (Не авторизация курьера с незаполнным обязательным полем)
        - def test_can_not_auth_login_not_found (Не авторизация курьера с не существующим логином в базе созданных пользователей)
    - test_order_list:
        - def test_get_orders_list (Получение списка заказов и возвращение тела ответа)
В проекте содержится отчет Allure (http://192.168.50.69:59620/index.html# Сформированный отчет в моей локальной сети)
