import time

import allure
from selenium.webdriver import ActionChains

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base import Base
from utilities.logger import Logger


class Headers_blocks(Base):

    url = 'https://www.a1.by/ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    # Locators

    logo_image = '/html/body/header/nav[2]/div/div[1]/a/span/img'
    private_customers_button = "//span[contains (text(), 'Частным клиентам')]"



    # Getters


    def get_logo_image(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.logo_image)))

    def get_private_customers_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.private_customers_button)))



    # Actions

    def click_logo_image(self):
        self.get_logo_image().click()
        print('Click logo image')


    def click_private_customers_button(self):
        self.get_private_customers_button().click()
        print('Click private_customers_button')
        self.driver.back()

    def action_button(self):
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.private_customers_button)))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        print("Cursor навелся")


    # Methods

    def headers_menu_elements(self):
        with allure.step('headers_menu_elements'):
            Logger.add_start_step(method='headers_menu_elements')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.get_screenshot()
            self.click_logo_image()
            self.action_button()
            time.sleep(5)
            self.click_private_customers_button()
            time.sleep(5)
            Logger.add_end_step(url=self.driver.current_url, method='headers_menu_elements')
