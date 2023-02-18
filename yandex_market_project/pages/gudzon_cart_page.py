import time
from lib2to3.pgen2 import driver
from telnetlib import EC

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class Gudzon_cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    product_word = "//span[@data-entity= 'basket-item-name']"
    price_word = "//span[@class = 'basket-item-price-current-text']"
    plus_button = "//span[@class = 'basket-item-amount-btn-plus']"
    order_button = "//*[@id='basket-root']/div[1]/div/div/div[2]/div/div[3]/button"
    product_word_order = "//span[@data-entity= 'basket-item-name']"
    price_word_order = "//*[@id='bx-soa-basket']/div[2]/div/div/div/div[2]/div[4]/div[2]/strong"



    # Getters
    def get_product_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_word)))

    def get_price_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_word)))

    def get_plus_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.plus_button)))

    def get_order_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_button)))

    def get_product_word_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_word_order)))

    def get_price_word_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_word_order)))


    # Actions

    def action_plus_button(self):
        self.get_plus_button().click()
        print("Click button 'Plus'")

    def action_order(self):
        self.get_order_button().click()
        print("Click button 'Cart'")




    # Methods
    def orderring(self):
        with allure.step('orderring'):
            Logger.add_start_step(method='orderring')
            self.get_current_url()
            self.scroll(0, 350)
            self.get_screenshot()
            self.assert_word(self.get_product_word(), 'Автомобильный магнитный держатель для телефона на воздуховод HOCO CA85, черный')
            self.assert_word(self.get_price_word(), '64.90 руб.')
            self.action_plus_button()
            self.action_order()
            print("-" * 100)
            self.assert_word(self.get_product_word_order(), 'Автомобильный магнитный держатель для телефона на воздуховод HOCO CA85, черный')
            self.scroll(0, 550)
            self.assert_word(self.get_price_word_order(), '129.80 руб.')
            print("-" * 100)
            Logger.add_end_step(url=self.driver.current_url, method='orderring')

# или через функцию replace: replace(старое_значение, новое_значение, количество_замен)