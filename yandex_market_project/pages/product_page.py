import time
from lib2to3.pgen2 import driver
from telnetlib import EC

import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class Product_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    product_word = "/html/body/div[4]/div[2]/div/div[4]/div/div/div[2]/div/div/div[1]/div[1]/h1"
    button_in_store = '/html/body/div[4]/div[2]/div/div[5]/div/div[2]/section/div[2]/div/div/div/div/div[2]/div[5]/div/a'


    # Getters
    def get_product_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_word)))

    def get_button_in_store(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_in_store)))



    # Actions
    def click_button_in_store(self):
        self.get_button_in_store().click()
        print("Click button 'In store'")



    # Methods
    def go_to_store(self):
        with allure.step('go_to_store'):
            Logger.add_start_step(method='go_to_store')
            self.tabbing()
            self.get_current_url()
            self.assert_word(self.get_product_word(), 'Магнитный держатель Hoco CA85 черный')
            self.click_button_in_store()
            self.tabbing()
            print("-" * 100)
            Logger.add_end_step(url=self.driver.current_url, method='go_to_store')


