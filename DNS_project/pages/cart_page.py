import time
from telnetlib import EC

from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import allure

from base.base import Base
from utilities.logger import Logger


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    # locators

    word = '//*[@id="cart-page-new"]/div[1]/div[2]/div/div/div[1]/div/div/div/div/div[1]/div[1]/div[1]/div[3]/div/div[1]/a'
    plus_button = '//*[@id="cart-page-new"]/div[1]/div[2]/div/div/div[1]/div/div/div/div/div[1]/div[1]/div[2]/div/button[2]/i'
    license_checkbox = '//*[@id="cart-page-new"]/div[1]/div[2]/div/div/div[1]/div/div/div/div/div[2]/div[1]/div[1]/div[2]/div/div/div/div[1]/label/span[1]'
    additional_product = '//*[@id="cart-page-new"]/div[1]/div[2]/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[1]/a'


    # Getters

    def get_product_word(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.word)))

    def get_plus_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.plus_button)))

    def get_license_checkbox(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.license_checkbox)))

    def get_additional_product(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.additional_product)))


    # Actions

    def click_plus_button(self):
        self.get_plus_button().click()
        print("Click plus button")

    def click_license_checkbox(self):
        self.get_license_checkbox().click()
        print("Click license checkbox")

    def click_additional_product(self):
        self.get_additional_product().click()
        print("Get additional product")



    # Methods

    def action_cart(self):
        with allure.step('action_cart'):
            Logger.add_start_step(method='action_cart')
            self.assert_url('https://www.dns-shop.ru/cart/')
            self.assert_word(self.get_product_word(), '15.6" Ноутбук HP Laptop 15s-fq2128ur серебристый')
            self.click_plus_button()
            self.click_license_checkbox()
            self.click_additional_product()
            self.tabbing()
            self.get_screenshot()
            print('-'*50)
            # time.sleep(5)
            Logger.add_end_step(url=self.driver.current_url, method='action_cart')
