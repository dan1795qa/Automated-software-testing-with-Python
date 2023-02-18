import time
from telnetlib import EC

from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import allure

from base.base import Base
from utilities.logger import Logger


class Main_page(Base):

    url = 'https://www.dns-shop.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    # locators

    input_search = "//input[@class = 'presearch__input']"

    # Getters

    def get_input_search(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.input_search)))


    # Actions

    def action_input_search(self, name_item):
        self.get_input_search().send_keys(name_item)
        print("Input search")


    def action_enter(self):
        self.get_input_search().send_keys(Keys.RETURN)
        print('Click "Enter"')



    # Methods

    def search_name_item(self):
        with allure.step('search_name_item'):
            Logger.add_start_step(method='search_name_item')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.action_input_search('Ноутбук')
            self.action_enter()
            self.scroll(0, 550)
            self.get_screenshot()
            print('-'*50)
            # time.sleep(5)
            Logger.add_end_step(url=self.driver.current_url, method='search_name_item')
