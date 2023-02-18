import time
from random import random, randrange, randint
from telnetlib import EC
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import allure
from base.base import Base
from utilities.logger import Logger
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

class Checkout_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    # locators

    check_orderring = '//*[@id="checkout"]/div/div[1]/div/div/div[2]'
    item_notebook = '//*[@id="checkout"]/div/div[1]/div/div/div[3]/div/div[1]/div[1]'
    item_license = "//div[contains(text(), 'Установка лицензионной ОС Windows (лицензия Windows приобретается отдельно) (1шт.)')]"
    item_mouse = "//div[contains(text(), 'Мышь беспроводная HP Wireless Mouse 200 серебристый (1шт.)')]"
    input_phone = "//div[@style = 'width: auto;']"
    input_name = "//*[@id='checkout']/div/div[2]/div[1]/div[2]/div[2]/div[3]/div/div/div"
    button_online = '//div[contains(text(), "Онлайн")]'
    select_bank_card = '//div[contains(text(), "Банковская карта")]'
    button_confirm = "//span[contains(text(), 'Подтвердить заказ')]"


    # Getters

    def get_check_orderring(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.check_orderring)))

    def get_check_item_notebook(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.item_notebook)))

    def get_check_item_license(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.item_license)))

    def get_check_item_mouse(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.item_mouse)))

    def get_input_phone(self):
        return WebDriverWait(self.driver, 35).until(EC.element_to_be_clickable((By.XPATH, self.input_phone)))

    def get_input_name(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.input_name)))

    def get_button_online(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.button_online)))

    def get_select_bank_card(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.select_bank_card)))

    def get_button_confirm(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.button_confirm)))


    # Actions

    def click_check_orderring(self):
        self.get_check_orderring().click()
        print("Click check orderring")

    def action_input_phone(self, name_phone):
        # self.get_input_phone().click()
        self.get_input_phone().send_keys(name_phone)
        print("Input phone")

        # ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
        # click_task_over = WebDriverWait(self.driver, 30, ignored_exceptions=ignored_exceptions) \
        #     .until(expected_conditions.presence_of_element_located((By.XPATH, self.input_phone)))
        # click_task_over().send_keys(name_phone)
        # click_task_over.click()

    def action_input_name(self, name):
        self.get_input_name().click()
        self.get_input_name().send_keys(name)
        print("Input name")

    def click_button_online(self):
        self.get_button_online().click()
        print("Click button online payment")

    def click_select_bank_card(self):
        self.get_select_bank_card().click()
        print("Click select bank card")

    def click_button_confirm(self):
        self.get_button_confirm().click()
        print("Click button confirm")



    # Methods

    def checkout(self):
        with allure.step('checkout'):
            Logger.add_start_step(method='checkout')
            self.assert_url('https://www.dns-shop.ru/checkout/')
            self.click_check_orderring()
            self.assert_word(self.get_check_item_notebook(), '15.6" Ноутбук HP Laptop 15s-fq2128ur серебристый (1шт.)')
            self.assert_word(self.get_check_item_license(), 'Установка лицензионной ОС Windows (лицензия Windows приобретается отдельно) (1шт.)')
            self.assert_word(self.get_check_item_mouse(), 'Мышь беспроводная HP Wireless Mouse 200 серебристый (1шт.)')
            self.click_check_orderring()
            # self.driver.refresh()
            self.action_input_phone('1234567891')
            self.action_input_name('Ivan')
            self.scroll(0, 850)
            self.click_button_online()
            self.click_select_bank_card()
            self.click_button_confirm()
            time.sleep(3)
            self.get_screenshot()
            print('-'*50)
            Logger.add_end_step(url=self.driver.current_url, method='checkout')
