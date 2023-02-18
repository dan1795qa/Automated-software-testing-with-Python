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


class Gudzon_product_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    product_word = "//*[@id='pagetitle']"
    button_to_cart = '//*[@id="bx_117848907_16755_basket_actions"]/span[1]'
    button_scroll = '//*[@id="scrollToTop"]'
    button_cart = '//*[@id="mobileheader"]/div[1]/div[3]/div[1]/div/a[3]/span/i/svg/use'
    icon_cart = '//*[@id="header"]/div[2]/div[1]/div/div/div[4]/div/div[3]'
    cart = '//*[@id="mobileheader"]/div[1]/div[3]/div[1]/div/a[3]'


    # Getters
    def get_product_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_word)))

    def get_button_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_to_cart)))

    def get_button_scroll(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_scroll)))

    def get_button_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.icon_cart)))




    # Actions
    def click_button_to_cart(self):
        self.get_button_to_cart().click()
        print("Click button 'In cart'")

    def click_button_scroll(self):
        self.get_button_scroll().click()
        print("Click button 'Scroll'")

    def action_icon_cart(self):
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.icon_cart)))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        print("Cursor навелся")


    def action_cart(self):
        self.get_button_cart().click()
        print("Click button 'Cart'")



    # Methods
    def go_to_cart(self):
        with allure.step('go_to_cart'):
            Logger.add_start_step(method='go_to_cart')
            self.get_current_url()
            self.scroll(0, 350)
            self.get_screenshot()
            self.assert_word(self.get_product_word(), 'Автомобильный магнитный держатель для телефона на воздуховод HOCO CA85, черный')
            self.click_button_to_cart()
            self.click_button_scroll()
            time.sleep(5)
            self.action_icon_cart()
            self.action_cart()
            print("-" * 100)
            Logger.add_end_step(url=self.driver.current_url, method='go_to_cart')


