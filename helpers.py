from faker import Faker
faker = Faker()


class GenerateCourierData:

    @staticmethod
    def generate_individual_courier_data():
        email = faker.email()
        password = faker.password()
        first_name = faker.first_name()
        payload = {
            "login": email,
            "password": password,
            "firstName": first_name
        }
        return payload

    @staticmethod
    def generate_courier_data_permanent():
        payload = {
            "login": "stormnew@yandex.ru",
            "password": "qwerty",
            "firstName": "Melany"
        }
        return payload
