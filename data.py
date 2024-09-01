
class UrlsData:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru/'
    CREATE_COURIER_ENDPOINT = 'https://qa-scooter.praktikum-services.ru/api/v1/courier'
    LOGIN_COURIER_ENDPOINT = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/login'
    CREATE_ORDER_ENDPOINT = 'https://qa-scooter.praktikum-services.ru/api/v1/orders'
    ORDER_LIST_ENDPOINT = 'https://qa-scooter.praktikum-services.ru/api/v1/orders'
    DELETE_COURIER_ENDPOINT = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/:id'


class TextsResponseData:
    SUCCESSFUL_CREATE_COURIER = '{"ok":true}'
    ERROR_LOGIN_ALREADY_USED = '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'
    ERROR_NOT_ENOUGH_DATA = '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'
    ERROR_NOT_ENOUGH_DATA_FOR_LOGIN = '{"code":400,"message":"Недостаточно данных для входа"}'
    ERROR_ACCOUNT_NOT_FOUND = '{"code":404,"message":"Учетная запись не найдена"}'


class OrderData:
    order_data = {
        "firstName": "Dmitriy",
        "lastName": "Golubkin",
        "address": "26 Laycock StLondon N1 1AH, UK",
        "metroStation": 1,
        "phone": "+44456443276",
        "rentTime": 7,
        "deliveryDate": "2024-01-01T21:00:00.000Z",
        "comment": "Call 10 minutes before delivery",
        "color": ["BLACK"]
    }

    scooter_color = [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ]
