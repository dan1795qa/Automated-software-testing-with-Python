import json

from requests import Response

""""Методы для проверки ответов наших запросов"""


class Checking():


    """"Метод для проверки статуса кода"""
    @staticmethod
    def check_status_code(result, status_code):

        # assert  status_code == result.status_code
        if result.status_code == status_code:
            print("Успешно!!! Статус код = " + str(result.status_code))
        else:
            print("Провал!!! Статус код = " + str(result.status_code))


    """"Метод для проверки наличия обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_token(result, expected_value):
        token = json.loads(result.text)              # преобразует в json
        assert list(token) == expected_value
        print("Все поля присутствуют")


    """"Метод для проверки наличия обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_value(result, field_name, expected_value):
        check = result.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name + " верен !!!")

    """"Метод для проверки наличия обязательных полей в ответе запроса по заданному слову"""
    @staticmethod
    def check_json_searc_word_in_value(result, field_name, search_word):
        check = result.json()
        check_info = check.get(field_name)
        if search_word in check_info:
            print("Слово " + search_word + " присутсвтует !!!")
        else:
            print("Слово " + search_word + " отсутствует !!!")

