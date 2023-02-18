import datetime
import time
from telnetlib import EC

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class Base():

    def __init__(self, driver):
        self.driver = driver

    """"Method get current url"""

    def get_current_url(self):
        print(f"Current url is: {self.driver.current_url}")


    """"Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")


    """"Method tabbing"""

    def tabbing(self):
        print(f"List tabs: {str(self.driver.window_handles)}")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])


    """"Method screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")  # Текущая дата
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\HP PAVILION\\PycharmProjects\\yandex_market_project\\screen\\' + name_screenshot)
        print("Screenshot: " + name_screenshot)


    """"Method scroll"""

    def scroll(self, x, y):
        self.driver.execute_script("window.scroll(" + str(x) + "," + str(y) + ")")
        print("Good scroll")
