import datetime
from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base():

    def __init__(self, driver):
        self.driver = driver


    """"Current url"""
    def get_current_url(self):
        url = self.driver.current_url
        print('Current: ' + url)

    """"Screenshot"""
    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")  # Текущая дата
        name_screenshot = 'screenshot ' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\HP PAVILION\\PycharmProjects\\project_A1\\screen\\' + name_screenshot)
        print("Screenshot: " + name_screenshot)

    """"Method assert word"""
    def assert_word(self, locator, result):
        word = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, locator)))
        value_word = word.text
        assert value_word == result
        print("Good value word")

    """"Method assert url"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")

    """"Method scroll"""
    def scroll(self, x, y):
        self.driver.execute_script("window.scroll(" + str(x) + ',' + str(y) +")")
        print("Good scroll ")

    """"Method tabbing"""
    def tabbing(self):
        print(f"List tabs: {str(self.driver.window_handles)}")
        # time.sleep(3)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    """"Method refresh and back"""
    def back_and_refresh(self):
        self.driver.back()
        self.driver.refresh()