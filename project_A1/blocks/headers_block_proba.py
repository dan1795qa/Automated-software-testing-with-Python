import allure

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base import Base
from utilities.logger import Logger


class Headers_blocks_proba(Base):

    url = 'https://www.a1.by/ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    # Locators

    logo_image = '/html/body/header/nav[2]/div/div[1]/a/span/img'
    private_customers_button = "//span[contains (text(), 'Частным клиентам')]"

    list_locators = [logo_image, private_customers_button]



    # Getters

    for i in list_locators:

        def get(self):
            return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.i)))

        # Actions

        def click_logo_image(self):
            self.get().click()
            print('Click logo image')




    # Methods

    def headers_menu_elements(self):
        with allure.step('headers_menu_elements'):
            Logger.add_start_step(method='headers_menu_elements')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            # self.get_screenshot()
            self.click_logo_image()
            Logger.add_end_step(url=self.driver.current_url, method='headers_menu_elements')
