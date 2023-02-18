import time
from lib2to3.pgen2 import driver
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class Market_search_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    input_search = "//input[@id='header-search']"
    search_checkbutton = "//button[@data-r='search-button']"
    price_min = "//label[contains(text(), 'от 5,62')]"
    price_max = "//label[contains(text(), 'до 170,54')]"
    producer_checkbutton = "//*[@id='searchFilters']/div/div[4]/div/div/div/div/div[3]/div/fieldset/div/div/div/div/div/div/div[2]/label/span/span[2]"
    type_checkbutton = "//*[@id='searchFilters']/div/div[4]/div/div/div/div/div[7]/div/fieldset/div/div/div/div/div/div/div[6]/label/span/span[2]"
    sale_checkbutton = "//span[contains(text(), 'В продаже')]"
    free_delivery_checkbutton = "//span[contains(text(), 'Бесплатно')]"
    product_choice = "//span[contains(text(), 'Hoco CA85 ')]"



    # Getters
    def get_search_area(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_search)))

    def get_search_checkbutton(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_checkbutton)))

    def get_price_min(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_min)))

    def get_price_max(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_max)))

    def get_producer_checkbutton(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.producer_checkbutton)))

    def get_type_checkbutton(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.type_checkbutton)))

    def get_sale_checkbutton(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sale_checkbutton)))

    def get_free_delivery_checkbutton(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.free_delivery_checkbutton)))

    def get_product_choice(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_choice)))


    # Actions
    def input_search_product(self, name_product):
        self.get_search_area().send_keys(name_product)
        print("Input product")

    def click_search_button(self):
        self.get_search_checkbutton().click()
        print("Click Search button")

    def input_price_min(self, name_price_min):
        # self.get_price_min().click()
        self.get_price_min().send_keys(name_price_min)
        print("Input Price min")

    def input_price_max(self, name_price_max):
        # self.get_price_max().click()
        self.get_price_max().send_keys(name_price_max)
        print("Input Price max")

    def click_producer_checkbutton(self):
        self.get_producer_checkbutton().click()
        print("Click producer checkbutton")

    def click_type_checkbutton(self):
        self.get_type_checkbutton().click()
        print("Click type checkbutton")

    def click_sale_checkbutton(self):
        self.get_sale_checkbutton().click()
        print("Click sale checkbutton")

    def click_free_delivery_checkbutton(self):
        self.get_free_delivery_checkbutton().click()
        print("Click free delivery checkbutton")

    def click_product_choice(self):
        self.get_product_choice().click()
        print("Click product choice")



    # Methods
    def search_product(self):
        with allure.step('search_product'):
            Logger.add_start_step(method='search_product')
            self.input_search_product('Автомобильные держатели')
            self.click_search_button()
            self.get_screenshot()
            self.get_current_url()
            self.scroll(0, 200)
            self.input_price_min('10')
            self.input_price_max('100')
            self.click_producer_checkbutton()
            self.scroll(0, 600)
            time.sleep(2)
            self.click_type_checkbutton()
            time.sleep(2)
            self.scroll(0, 1800)
            time.sleep(2)
            self.click_sale_checkbutton()
            time.sleep(2)
            self.click_free_delivery_checkbutton()
            time.sleep(2)
            self.scroll(0, -1200)
            self.click_product_choice()
            print("-" * 100)
            Logger.add_end_step(url=self.driver.current_url, method='search_product')

