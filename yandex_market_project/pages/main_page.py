import time
from lib2to3.pgen2 import driver
from telnetlib import EC

import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilities.logger import Logger


class Main_page(Base):

    url = 'https://yandex.by/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    menu_services = "//a[@class='home-link2 services-pinned__item services-pinned__all']"
    menu_more_services = "/html/body/div[2]/div/div/div[1]/div/div[4]/a[1]"
    button_market = "//span[@id='services-big-item-market-title']"
    main_word = "//*[@id='logoPartMarket']"


    # Getters
    def get_services(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu_services)))

    def get_more_services(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu_more_services)))

    def get_market(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_market)))

    def get_main_word(self):
        return  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))


    # Actions
    def click_services(self):
        self.get_services().click()
        print("Click services")

    def click_more_services(self):
        self.get_more_services().click()
        print("Click more services")

    def click_button_market(self):
        self.get_market().click()
        print("Click button market")


    # Methods
    def go_to_market(self):
        with allure.step('go_to_market'):
            Logger.add_start_step(method='go_to_market')
            print("-" * 100)
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_services()
            self.click_more_services()
            print("-" * 100)
            self.tabbing()
            self.get_current_url()
            self.click_button_market()
            self.assert_word(self.get_main_word(), 'Яндекс Маркет')
            self.get_screenshot()
            self.get_current_url()
            print("-"*100)
            Logger.add_end_step(url=self.driver.current_url, method='go_to_market')


