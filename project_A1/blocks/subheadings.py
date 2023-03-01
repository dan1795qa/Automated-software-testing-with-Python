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

    go_to_A1_button = "//span[contains (text(), 'Перейти в А1')]"
    assert_go_to_A1_button = "//span[contains (text(), 'Добро пожаловать в сеть А1 со своим номером')]"

    go_to_A1 = "//span[contains (text(), 'Перейти в А1')]"
    assert_go_to_A1 = "//span[contains (text(), 'Добро пожаловать в сеть А1 со своим номером')]"

    internet_shop_button = "//span[contains (text(), 'Интернет-магазин')]"
    assert_internet_shop_button = "//h2[contains (text(), 'Товары по акции')]"

    video_service_VOKA_button = "//span[contains (text(), 'Видеосервис VOKA')]"
    assert_video_service_VOKA_button = "//h1[contains (text(), 'Тарифы Трансляции ТВ в Минске')]"

    fin_services_button = "//span[contains (text(), 'Финансовые сервисы')]"
    assert_fin_services_button = "//h1[contains (text(), 'Услуги')]"


    # Getters

    def get_tariffs_and_services_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.tariffs_and_services_button)))

    def get_go_to_A1(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.go_to_A1_button)))

    def get_internet_shop_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.internet_shop_button)))

    def get_video_service_VOKA_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.video_service_VOKA_button)))

    def get_fin_services_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.fin_services_button)))



    # Actions

    def click_tariffs_and_services_button(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.tariffs_and_services_button)))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        print("Move to element success")

        self.get_tariffs_and_services_button().click()
        print('Click tariffs_and_services_button')

    def click_go_to_A1_button(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.go_to_A1_button)))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        print("Move to element success")

        self.get_go_to_A1().click()
        print('Click go_to_A1_button')

    def click_internet_shop_button(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.internet_shop_button)))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        print("Move to element success")

        self.get_internet_shop_button().click()
        print('Click internet_shop_button')

    def click_video_service_VOKA_button(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.video_service_VOKA_button)))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        print("Move to element success")

        self.get_video_service_VOKA_button().click()
        print('Click video_service_VOKA_button')

    def click_fin_services_button(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.fin_services_button)))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        print("Move to element success")

        self.get_fin_services_button().click()
        print('Click fin_services_button')


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

            self.click_go_to_A1_button()
            self.assert_url('https://www.a1.by/ru/services/other-services/perehod-na-a1/p/perehod_na_a1')
            self.assert_word(self.assert_go_to_A1_button, 'Добро пожаловать в сеть А1 со своим номером')
            self.get_screenshot()
            self.back_and_refresh()
            print('-' * 100)

            self.click_internet_shop_button()
            self.assert_url('https://www.a1.by/ru/c/shop')
            self.assert_word(self.assert_internet_shop_button, 'Товары по акции')
            self.get_screenshot()
            self.back_and_refresh()
            print('-' * 100)

            self.click_video_service_VOKA_button()
            print(f"List tabs: {str(self.driver.window_handles)}")
            self.driver.switch_to.window(self.driver.window_handles[1])
            print('Switch to window success')
            self.assert_url('https://internet.a1.by/minsk/iptv')
            # self.scroll(0 , 500)
            self.assert_word(self.assert_video_service_VOKA_button, 'Тарифы Трансляции ТВ в Минске')
            self.get_screenshot()
            self.driver.close()
            time.sleep(1)
            self.driver.switch_to.window(self.driver.window_handles[0])
            # self.back_and_refresh()
            print('-' * 100)

            self.click_fin_services_button()
            self.assert_url('https://www.a1.by/ru/services/c/Fin_uslugi')
            self.assert_word(self.assert_fin_services_button, 'Услуги')
            self.get_screenshot()
            self.back_and_refresh()
            print('-' * 100)

            Logger.add_end_step(url=self.driver.current_url, method='subheadings_menu_elements')