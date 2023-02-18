import requests

class New_location():

    """"Работа с пятью локациями"""

    def test_delete_new_location(self):

        """"Удаление 2-ой и 4-ой  локаций и запись оставшихся place_id в файл new_file_api_place_id.txt"""

        print("Старт удаления локаций!")
        print('-' * 150)
        base_url = "https://rahulshettyacademy.com"
        key = "?key=qaclick123"

        """"Удаление новой локации"""

        delete_resource = "/maps/api/place/delete/json"
        delete_url = base_url + delete_resource + key
        print(delete_url)


        fr = open('file_api_place_id.txt', 'r')
        place_id = fr.read()
        fr.close()

        place_id_list = place_id.split('\n')
        # print(place_id_list)

        for place_id in place_id_list:

            if place_id == place_id_list[1] or place_id == place_id_list[3]:

                json_for_delete_location = {
                    "place_id": place_id
                }

                result_delete = requests.delete(delete_url, json=json_for_delete_location)
                print(result_delete.text)

                print("Статус код: " + str(result_delete.status_code))
                assert 200 == result_delete.status_code

                check_status = result_delete.json()
                check_info_status = check_status.get("status")
                print("Сообщение: " + check_info_status)
                assert check_info_status == 'OK'
                print("Локация " + place_id + " успешно удалена!!!")
                print('-' * 150)
                print("Удаление локации завершено!")

            else:
                print('-' * 150)

        """"Проверка наличия существующих и несуществующих локаций"""

        print('-' * 150)
        print("Старт проверки наличия локаций!")
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
            if result_get.status_code == 200:
                print("Локация " + place_id + " существует")
                fw = open('new_file_api_place_id.txt', 'a')
                fw.write(place_id + "\n")
                fw.close()
                print('-' * 150)
            else:
                check_msg = result_get.json()
                check_info_msg = check_msg.get("msg")
                print("Сообщение: " + check_info_msg)
                assert check_info_msg == "Get operation failed, looks like place_id  doesn't exists"
                print("Локация " + place_id + " не найдена")
                print('-' * 150)


        print('-' * 150)
        print("Проверка на наличие локаций завершено!")
        print('-' * 150)


new_place = New_location()
new_place.test_delete_new_location()