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


    """"Метод по созданию одной шутке на каждую тему"""
    def creating_one_joke_per_topic(self):

        url = "https://api.chucknorris.io/jokes/categories"
        result = requests.get(url)
        result_list = result.json()

        """"Прогон цикла запросов по одной шутке на каждую тему"""
        for joke_cathegories in result_list:

            url = "https://api.chucknorris.io/jokes/random?category=" + joke_cathegories
            print(url)
            result = requests.get(url)
            print("Статус код: " + str(result.status_code))

            assert 200 == result.status_code
            print("Успешно!!! Мы получили новую шутку по теме '" +  joke_cathegories + "'")

            result.encoding = 'utf-8'
            print("Тело ответа: \n" + str((result.json())))

            print('\n' + '-' * 150 + '\n')



test_1 = Joke()
test_1.test_get_cathegories()

test_2 = Joke()
test_2.creating_one_joke_per_topic()
