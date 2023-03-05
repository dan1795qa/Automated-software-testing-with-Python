import time
from selenium import webdriver
import allure
from selenium.webdriver import ActionChains, Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base import Base
from utilities.logger import Logger


class Subheadings_right(Base):

    url = 'https://www.a1.by/ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    """"Search input"""
    # Locators
    search_input = '//*[@id="dropdownGlobalSearch"]/span'
    area_search_input = '//*[@id="i-global-search-input"]'
    assert_search_input = '//h1[contains (text(), "Результаты поиска для «Тарифы»")]'

    # Getters
    def get_search_input(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.search_input)))

    def get_area_search_input(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.area_search_input)))

    # Actions
    def input_search_input(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.search_input)))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        print("Move to element success")
        self.get_search_input().click()
        print('Click search_input')
        self.get_area_search_input().send_keys('Тарифы')
        self.get_area_search_input().send_keys(Keys.RETURN)
        print('Input text in search area')
        self.assert_url('https://www.a1.by/ru/search?text=%D0%A2%D0%B0%D1%80%D0%B8%D1%84%D1%8B')
        self.assert_word(self.assert_search_input, 'Результаты поиска для «Тарифы»')


    """"Icon_questions"""
    # Locators
    icon_questions = '//*[@id="dropdownMenuContactsForm"]/span'

    ask_questions = '/html/body/header/nav[2]/div/div[2]/div[2]/div/div[1]/button[1]'
    assert_ask_questions = '//div[contains (text(), "Для начала диалога введите, пожалуйста, свою контактную информацию и вопрос.")]'
    close_window_ask_questions = '//*[@id="webim_chat"]/div[1]/div/div'

    questions = '/html/body/header/nav[2]/div/div[2]/div[2]/div/div[1]/button[2]'
    assert_questions = '//h1[contains (text(), "Задать вопрос по покрытию")]'

    vk_link = '//span[contains (text(), "Вконтакте")]'
    assert_vk_link = '//div[contains (text(), "Чтобы просматривать эту страницу, нужно зайти на сайт.")]'

    fb_link = '//span[contains (text(), "Facebook")]'
    assert_fb_link = '//h2[contains (text(), "Будьте на связи с важными для вас людьми.")]'

    ok_link = '//span[contains (text(), "Одноклассники")]'
    assert_ok_link = '//div[contains (text(), "Нет профиля в Одноклассниках")]'


    # Getters
    def get_icon_questions(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.icon_questions)))

    def get_ask_questions(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.ask_questions)))

    def get_close_window_ask_questions(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.close_window_ask_questions)))

    def get_questions(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.questions)))

    def get_vk_link(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.vk_link)))

    def get_fb_link(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.fb_link)))

    def get_ok_link(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.ok_link)))

    # Actions
    def click_icon_questions(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.icon_questions)))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        print("Move to element success")
        self.get_icon_questions().click()
        print('Click icon_questions')

    def click_ask_questions(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.ask_questions)))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        print("Move to element success")
        self.get_ask_questions().click()
        print('Click ask_questions')
        self.assert_word(self.assert_ask_questions, 'Для начала диалога введите, пожалуйста, свою контактную информацию и вопрос.')
        self.get_close_window_ask_questions().click()

    def click_questions(self):
        self.get_icon_questions().click()
        print('Click icon_questions')
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.questions)))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        print("Move to element success")
        self.get_questions().click()
        print('Click questions')
        self.assert_url('https://www.a1.by/ru/company/coverage-ask-question')
        self.assert_word(self.assert_questions, 'Задать вопрос по покрытию')

    def click_vk_link(self):
        self.get_icon_questions().click()
        print('Click icon_questions')
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.vk_link)))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        print("Move to element success")
        self.get_vk_link().click()
        print('Click vk_link')
        print(f"List tabs: {str(self.driver.window_handles)}")
        self.driver.switch_to.window(self.driver.window_handles[1])
        # self.assert_url('https://vk.com/login?u=2&to=L3dyaXRlLTM1ODMxMDI-')
        self.assert_word(self.assert_vk_link, 'Чтобы просматривать эту страницу, нужно зайти на сайт.')
        self.get_screenshot()
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])


    def click_fb_link(self):
        self.get_icon_questions().click()
        print('Click icon_questions')
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.fb_link)))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        print("Move to element success")
        self.get_fb_link().click()
        print('Click fb_link')
        print(f"List tabs: {str(self.driver.window_handles)}")
        self.driver.switch_to.window(self.driver.window_handles[1])
        # self.assert_url('https://www.messenger.com/login.php?next=https%3A%2F%2Fwww.messenger.com%2Ft%2F223113717743177%2F%3Fmessaging_source%3Dsource%253Apages%253Amessage_shortlink%26source_id%3D1441792%26recurring_notification%3D0')
        self.assert_word(self.assert_fb_link, 'Будьте на связи с важными для вас людьми.')
        self.get_screenshot()
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def click_ok_link(self):
        self.get_icon_questions().click()
        print('Click icon_questions')
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.ok_link)))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        print("Move to element success")
        self.get_ok_link().click()
        print('Click ok_link')
        print(f"List tabs: {str(self.driver.window_handles)}")
        self.driver.switch_to.window(self.driver.window_handles[1])
        # self.assert_url('https://ok.ru/dk?st.cmd=anonymMain&st.lgi=WYL93Tgz1t4H')
        self.assert_word(self.assert_ok_link, 'Нет профиля в Одноклассниках')
        self.get_screenshot()
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])


    """"Cart"""
    # Locators
    cart = '//*[@id="mini-cart-loader-2"]'
    assert_cart = '//h1[contains (text(), "Корзина")]'

    # Getters
    def get_cart(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    # Actions

    def click_cart(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart)))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        print("Move to element success")
        self.get_cart().click()
        print('Click cart')
        self.assert_url('https://www.a1.by/ru/cart')
        self.assert_word(self.assert_cart, 'Корзина')



    # """"User_profile"""
    # # Locators
    # user_profile = '//*[@id="dropdownMenuUser"]/span'
    #
    # # Getters
    # def get_user_profile(self):
    #     return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.user_profile)))
    #
    #
    #
    # # Actions
    #
    # def input_search_input(self):
    #     element = WebDriverWait(self.driver, 30).until(
    #         EC.element_to_be_clickable((By.XPATH, self.search_input)))
    #     hover = ActionChains(self.driver).move_to_element(element)
    #     hover.perform()
    #     print("Move to element success")
    #
    #     self.get_search_input().click()
    #     print('Click fin_services_button')
    #
    #     self.get_area_search_input().send_keys('Тарифы')
    #     self.get_area_search_input().send_Keys(Keys.RETURN)
    #     print('Input text in search area')
    #

    # Methods

    def subheadings_menu_elements_right(self):
        with allure.step('subheadings_menu_elements_right'):
            Logger.add_start_step(method='subheadings_menu_elements_right')

            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.get_screenshot()
            print('-' * 100)

            self.input_search_input()
            self.get_screenshot()
            self.back_and_refresh()
            print('-' * 100)

            self.click_icon_questions()
            self.get_screenshot()
            self.click_ask_questions()
            self.get_screenshot()
            self.click_questions()
            self.get_screenshot()
            self.back_and_refresh()
            self.click_vk_link()
            self.click_fb_link()
            self.click_ok_link()
            # self.back_and_refresh()
            print('-' * 100)

            self.click_cart()
            self.get_screenshot()
            self.back_and_refresh()
            print('-' * 100)



            print('-' * 100)

            # self.click_video_service_VOKA_button()
            # print(f"List tabs: {str(self.driver.window_handles)}")
            # self.driver.switch_to.window(self.driver.window_handles[1])
            # print('Switch to window success')
            # self.assert_url('https://internet.a1.by/minsk/iptv')
            # # self.scroll(0 , 500)
            # self.assert_word(self.assert_video_service_VOKA_button, 'Тарифы Трансляции ТВ в Минске')
            # self.get_screenshot()
            # self.driver.close()
            # time.sleep(1)
            # self.driver.switch_to.window(self.driver.window_handles[0])
            # # self.back_and_refresh()
            # print('-' * 100)


            Logger.add_end_step(url=self.driver.current_url, method='subheadings_menu_elements_right')