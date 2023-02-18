import time
from telnetlib import EC

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import allure

from base.base import Base
from utilities.logger import Logger


class Additional_product_cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    # locators

    picture_1 = '//*[@id="tns1-item1"]/picture/img'
    picture_2 = '//*[@id="tns1-item2"]/picture/img'
    picture_5 = '//*[@id="tns1-item5"]/picture/img'
    comment = "//span[contains(text(), 'Комментарии ')]"
    button_buy = "//button[contains(text(), 'Купить')]"
    icon_cart = "//*[@id='app-cart-modal']"
    button_order = "//*[@id='app-cart-modal']/div/div[2]/div[2]/button[1]"


    # Getters

    def get_in_comment(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.comment)))

    def get_button_buy(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.button_buy)))

    def get_button_order(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.button_order)))




    # Actions

    def action_icon_mouse_1(self):
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.picture_1)))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        print("Cursor move to element 1")
        time.sleep(3)

    def action_icon_mouse_2(self):
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.picture_2)))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        print("Cursor move to element 2")
        time.sleep(3)

    def action_icon_mouse_5(self):
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.picture_5)))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        print("Cursor move to element 5")
        time.sleep(3)

    def click_comment(self):
        self.get_in_comment().click()
        print("Click in comment")

    def click_button_buy(self):
        self.get_button_buy().click()
        print("Click in button buy")

    def action_icon_cart(self):
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.icon_cart)))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        print("Cursor move to cart")

    def click_button_order(self):
        self.get_button_order().click()
        print("Click in button order")




    # Methods

    def action_additional_product_cart(self):
        with allure.step('action_additional_product_cart'):
            Logger.add_start_step(method='action_additional_product_cart')
            self.assert_url('https://www.dns-shop.ru/product/3287191d12ba3330/mys-besprovodnaa-hp-wireless-mouse-200-serebristyj/')
            self.scroll(0, 250)
            self.action_icon_mouse_1()
            self.action_icon_mouse_2()
            self.action_icon_mouse_5()
            self.scroll(0, 1500)
            self.click_comment()
            self.driver.refresh()
            self.scroll(0, -1500)
            self.click_button_buy()
            self.action_icon_cart()
            self.click_button_order()
            self.get_screenshot()
            print('-'*50)
            Logger.add_end_step(url=self.driver.current_url, method='action_additional_product_cart')
