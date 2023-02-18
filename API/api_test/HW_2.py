import requests

""""Создание класса """
class Joke():

    def __init__(self):
        pass


    """"Получение категорий"""
    def test_get_cathegories(self):

        url = "https://api.chucknorris.io/jokes/categories"
        print(url)
        result = requests.get(url)
        print("Статус код: " + str(result.status_code))

        assert 200 == result.status_code
        print("Успешно!!! Мы получили список категорий")

        result.encoding = 'utf-8'
        result_list = result.json()
        print(result_list)
        print('\n' + '-'*150)
        print('-'*150 + '\n')


    """"Запрос по созданию шутки на существующую и несущесвтующую категорию"""
    def creating_joke_custom_theme(self):

        url = "https://api.chucknorris.io/jokes/categories"
        result = requests.get(url)
        result_list = result.json()

        name_cathegory = input("Введите категорию шутки(несколько названий вводите через пробел!!!): ")
        name_cathegory_list = name_cathegory.split(" ")

        for cathegory in name_cathegory_list:
            if cathegory in result_list:
                print("Данная категория существует!")
                url_cathegory = "https://api.chucknorris.io/jokes/random?category=" + cathegory
                print(url_cathegory)
                result = requests.get(url_cathegory)
                print("Статус код: " + str(result.status_code))

                assert result.status_code == 200
                print("Успешно!!! Мы получили новую шутку по теме '" + cathegory + "'")

                result.encoding = 'utf-8'
                print("Тело ответа: \n" + str((result.json())))

                print('\n' + '-' * 150 + '\n')
            else:
                print("Категории " + cathegory + " не существует!")
                url_cathegory = "https://api.chucknorris.io/jokes/random?category=" + cathegory
                print(url_cathegory)
                result = requests.get(url_cathegory)
                print("Статус код: " + str(result.status_code))

                print('\n' + '-' * 150 + '\n')


test_1 = Joke()
test_1.test_get_cathegories()

test_2 = Joke()
test_2.creating_joke_custom_theme()
