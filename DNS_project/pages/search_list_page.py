import time
from telnetlib import EC
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import allure
from base.base import Base
from utilities.logger import Logger
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException


class Search_list_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # locators

    input_price_min = "/html/body/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/div[4]/div/div/div[1]/input"
    input_price_max = "/html/body/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/div[4]/div/div/div[2]/input"
    show_all = '/html/body/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/div[6]/div/div/a[1]/span'
    producer_asus = "/html/body/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/div[6]/div/div/div[2]/label[7]/span[2]"
    producer_hp = "/html/body/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/div[6]/div/div/div[2]/label[19]/span[2]"
    os = "//span[contains(text(), 'Операционная система')]"
    select_os = "//span[contains(text(), 'без ОС  ')]"
    apply_button = '/html/body/div[2]/div/div[2]/div[1]/div/div[3]/div[2]/div/button[1]'
    button = "/html/body/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[4]/button[2]"
    cart_button = '/html/body/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[4]/button[2]'

    # Getters

    def get_input_price_min(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.input_price_min)))

    def get_input_price_max(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.input_price_max)))

    def get_show_all_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.show_all)))

    def get_producer_asus(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.producer_asus)))

    def get_producer_hp(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.producer_hp)))

    def get_os(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.os)))

    def get_select_os(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.select_os)))

    def get_apply_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.apply_button)))

    def get_buy_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.button)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    # Actions

    def action_input_price_min(self, prcie_min):
        self.get_input_price_min().send_keys(prcie_min)
        print('Input: ' + prcie_min)

    def action_input_price_max(self, price_max):
        self.get_input_price_max().send_keys(price_max)
        print('Input: ' + price_max)

    def action_show_all_button(self):
        self.get_show_all_button().click()
        print('Click show all')

    def check_producer_asus(self):
        self.get_producer_asus().click()
        print('Click producer asus')

    def check_producer_hp(self):
        self.get_producer_hp().click()
        print('Click producer hp')

    def check_click_os(self):
        self.get_os().click()
        print('Click os')

    def check_click_select_os(self):
        self.get_select_os().click()
        print('Click select os')

    def click_apply_button(self):
        self.get_apply_button().click()
        print('Click apply button')

    def click_buy_button(self):
        self.get_buy_button().click()
        print('Click buy button')

    def click_cart_button(self):
        self.get_cart_button().click()
        print('Click cart button')



    # Methods


    def filter_notebook(self):
        with allure.step('filter_notebook'):
            Logger.add_start_step(method='filter_notebook')
            self.get_current_url()
            self.scroll(0, 500)
            self.action_input_price_min('20500')
            self.action_input_price_max('80500')
            self.scroll(0, 950)
            self.action_show_all_button()
            self.check_producer_asus()
            self.check_producer_hp()
            self.scroll(0, 1850)
            self.check_click_os()
            self.check_click_select_os()
            self.scroll(0, 400)
            self.click_apply_button()
            self.scroll(0, -2000)
            self.driver.refresh()
            self.click_buy_button()
            time.sleep(3)
            self.click_cart_button()
            time.sleep(3)
            self.get_screenshot()
            print('-'*50)
            Logger.add_end_step(url=self.driver.current_url, method='filter_notebook')
