import requests

class Swapi_heroes():

    """"Запрос на получения списка персонажей котоые снимались в фильмах вместе с "Darth Vader" """
    def test_get_characters(self):

        """"Запрос на получения списка фильмов где снимался "Darth Vader" """
        global check_info_value

        base_url = "https://swapi.dev/api/"
        resource = "people/4/"
        get_url = base_url + resource
        print(get_url)

        result_get = requests.get(get_url)
        print("Статус код: " + str(result_get.status_code))

        result_get_json = result_get.json()
        list_url_films = result_get_json.get("films")
        print("Список фильмов: ")
        print(list_url_films)
        print('-' * 150)


        for film in list_url_films:
            """"Запрос на получения списка персонажей которые снимались с "Darth Vader" по каждому фильму """
            result_film_get = requests.get(film)
            check = result_film_get.json()
            check_info_value = check.get('characters')
            print("Персонажи которые снимались в фильме: " + film)
            print(check_info_value)
            print('-'*150)

        """"Получение общего списка персонажей которые снимались вместе с "Darth Vader" и запись списка в файл"""
        print('-' * 150)
        set_characters = set(check_info_value)
        print("Список персонажей которые снимались вместе с 'Darth Vader': ")
        list_characters = list(set_characters)
        print(list_characters)

        fr = open('file_characters.txt', 'a')
        fr.write("\n".join(list_characters))
        fr.close()


test = Swapi_heroes()
test.test_get_characters()