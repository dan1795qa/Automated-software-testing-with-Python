import time
from selenium import webdriver
import allure
from selenium.webdriver import ActionChains

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base import Base
from utilities.logger import Logger


class Subteadings(Base):

    url = 'https://www.a1.by/ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    tariffs_and_services_button = "//span[contains (text(), 'Тарифы и услуги')]"
    assert_tariffs_and_services_button = "//h2[contains (text(), 'Тарифы и услуги')]"

    go_to_A1 = "//span[contains (text(), 'Перейти в А1')]"
    assert_go_to_A1 = "//span[contains (text(), 'Добро пожаловать в сеть А1 со своим номером')]"


    # Getters

    def get_tariffs_and_services_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.tariffs_and_services_button)))

    def get_go_to_A1(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.go_to_A1)))


    # Actions

    def click_tariffs_and_services_button(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.tariffs_and_services_button)))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        print("Move to element success")

        self.get_tariffs_and_services_button().click()
        print('Click logo image')

    def click_go_to_A1(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.go_to_A1)))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        print("Move to element success")

        self.get_go_to_A1().click()
        print('Click logo image')



    # Methods

    def subheadings_menu_elements(self):
        with allure.step('subheadings_menu_elements'):
            Logger.add_start_step(method='subheadings_menu_elements')

            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.get_screenshot()
            print('-' * 100)

            self.click_tariffs_and_services_button()
            self.assert_url('https://www.a1.by/ru/tarify-uslugi')
            self.assert_word(self.assert_tariffs_and_services_button, 'Тарифы и услуги')
            self.get_screenshot()
            self.back_and_refresh()
            print('-' * 100)

            self.click_go_to_A1()
            self.assert_url('https://www.a1.by/ru/services/other-services/perehod-na-a1/p/perehod_na_a1')
            self.assert_word(self.assert_go_to_A1, 'Добро пожаловать в сеть А1 со своим номером')
            self.get_screenshot()
            self.back_and_refresh()
            print('-' * 100)


            Logger.add_end_step(url=self.driver.current_url, method='subheadings_menu_elements')