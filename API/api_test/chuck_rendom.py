import requests

class New_joke():
    """"Создание новой шутки"""

    def __init__(self):
        pass

    def test_create_new_random_joke(self):
        """"Создание случайной шутки"""
        url = "https://api.chucknorris.io/jokes/random"
        print(url)
        result = requests.get(url)
        print("Статус код: " + str(result.status_code))

        assert 200 == result.status_code
        print("Успешно!!! Мы получили новую шутку")

        result.encoding = 'utf-8'
        print(result.text)

        check = result.json()
        check_info = check.get("categories")
        print(check_info)
        assert check_info == []
        print("Категория верна")

        check_info_value = check.get("value")
        print(check_info_value)
        name = 'Chuck'
        if name in check_info_value:
            print('Chuck присутствует')
        else:
            print('Chuck отсуствует')



    def test_create_new_random_cathegory_joke(self):
        """"Создание случайной шутки на определенную тему"""
        cathegory = 'sport'
        url = "https://api.chucknorris.io/jokes/random?category=" + cathegory
        print(url)
        result = requests.get(url)
        print("Статус код: " + str(result.status_code))

        assert 200 == result.status_code

        print("Успешно!!! Мы получили новую шутку")

        result.encoding = 'utf-8'
        print(result.text)

        check = result.json()
        check_info = check.get("categories")
        print(check_info)
        assert check_info == ['sport']
        print("Категория верна")

        check_info_value = check.get("value")
        print(check_info_value)
        name = 'Chuck'
        if name in check_info_value:
            print('Chuck присутствует')
        else:
            print('Chuck отсуствует')

random_joke = New_joke()
# random_joke.test_create_new_random_joke()


sport_joke = New_joke()
sport_joke.test_create_new_random_cathegory_joke()