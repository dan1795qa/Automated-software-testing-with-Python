import requests

class New_location():

    """"Работа с новой локацией"""

    def test_create_new_location(self):

        """"Создание 5(пяти) новых локаций и запись place_id в файл file_api_place_id.txt"""

        print("Старт создания новых локаций!")
        print('-' * 150)
        base_url = "https://rahulshettyacademy.com"
        key = "?key=qaclick123"

        count_requests = 5

        while count_requests >= 1:

            """"Создание новой локации"""

            post_resource = "/maps/api/place/add/json"
            post_url = base_url + post_resource + key
            print(post_url)

            json_for_create_new_location = {
                "location": {
                    "lat": -38.383494,
                    "lng": 33.427362
                }, "accuracy": 50,
                "name": "Frontline house",
                "phone_number": "(+91) 983 893 3937",
                "address": "29, side layout, cohen 09",
                "types": [
                    "shoe park",
                    "shop"
                ],
                "website": "http://google.com",
                "language": "French-IN"
            }

            result_post = requests.post(post_url, json=json_for_create_new_location)
            print(result_post.text)

            print("Статус код: " + str(result_post.status_code))
            assert 200 == result_post.status_code
            print("Успешно!!! Cоздана новая локация")

            check_post = result_post.json()
            check_info_post = check_post.get("status")
            print(check_info_post)
            print("Статус код ответа: " + check_info_post)
            assert check_info_post == "OK"
            print("Статус ответа верен")
            place_id = check_post.get("place_id")
            print("Place_id: " + place_id)

            fw = open('file_api_place_id.txt', 'a')
            if count_requests == 1:
                fw.write(place_id)
                fw.close()
            else:
                fw.write(place_id + "\n")
                fw.close()

            print('-'*150)

            count_requests -= 1

        print("Создание новых локаций завершено!")
        print('-' * 150)


        """"Проверка создания 5(пяти) новых локаций"""

        print("Старт проверки созданных локаций!")
        print('-' * 150)

        fr = open('file_api_place_id.txt', 'r')
        place_id = fr.read()
        fr.close()
        place_id_list = place_id.split('\n')

        for place_id in place_id_list:

            get_resource = "/maps/api/place/get/json"
            get_url = base_url + get_resource + key + '&place_id=' + place_id
            print(get_url)
            result_get = requests.get(get_url)
            print(result_get.text)

            print("Статус код: " + str(result_get.status_code))
            assert 200 == result_get.status_code
            print("Успешно!!! Проверка создания новой локации прошла успешно")

            print('-' * 150)
        print("Проверка созданных локаций завершено!")
        print('-' * 150)


new_place = New_location()
new_place.test_create_new_location()