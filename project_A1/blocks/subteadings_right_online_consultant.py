import time
from selenium import webdriver
import allure
from selenium.webdriver import ActionChains, Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base import Base
from utilities.logger import Logger


class Subheadings_right_online_consultant(Base):

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

    your_name_input = '//*[@id="webim_chat"]/div[3]/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[2]/div/div[1]/div/div[1]/div[1]/label/input'
    phone_input = '//*[@id="webim_chat"]/div[3]/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[2]/div/div[1]/div/div[1]/div[2]/label/input'
    mail_input = '//*[@id="webim_chat"]/div[3]/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[2]/div/div[1]/div/div[1]/div[3]/label/input'
    personal_account_input = '//*[@id="webim_chat"]/div[3]/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[2]/div/div[1]/div/div[1]/div[4]/label/input'
    message_area = '//*[@id="webim_chat"]/div[3]/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[2]/div/div[1]/div/div[2]/label/textarea'
    agree_checkbox = '//*[@id="webim_chat"]/div[3]/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[2]/div/div[1]/div/div[3]/label/svg[1]'
    agree_checkbox_text = "assert_search_input = '//h1[contains (text(), 'Согласен на сбор, хранение, обработку персональных данных')]"
    assert_agree_checkbox_text = "//h1[contains (text(), 'Другие документы')]"
    begin_talk_button = "//button[contains (text(), 'Начать диалог')]"

    close_window_ask_questions = '//*[@id="webim_chat"]/div[1]/div/div'


    # Getters
    def get_icon_questions(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.icon_questions)))

    def get_ask_questions(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.ask_questions)))

    def get_your_name_input(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.your_name_input)))

    def get_phone_input(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.phone_input)))

    def get_mail_input(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.mail_input)))

    def get_personal_account_input(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.personal_account_input)))

    def get_message_area(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.message_area)))

    def get_agree_checkbox(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.agree_checkbox)))

    def get_agree_checkbox_text(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.agree_checkbox_text)))

    def get_begin_talk_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.begin_talk_button)))

    def get_close_window_ask_questions(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.close_window_ask_questions)))



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

    def input_your_name_input(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.your_name_input)))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        print("Move to element success")
        self.get_your_name_input().send_keys('daniil')
        print('Input your_name_input')

    def input_phone_input(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.phone_input)))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        print("Move to element success")
        self.get_phone_input().send_keys('375331111111')
        print('Input phone_input')

    def input_mail_input(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.mail_input)))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        print("Move to element success")
        self.get_mail_input().send_keys('dan@gmail.com')
        print('Input mail_input')

    def input_personal_account_input(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.personal_account_input)))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        print("Move to element success")
        self.get_personal_account_input().send_keys('123456789')
        print('Input personal_account_input')

    def input_message_area(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.message_area)))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        print("Move to element success")
        self.get_message_area().send_keys('Hello, I have problem!!!')
        print('Input message_area')

    def input_agree_checkbox(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.agree_checkbox)))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        print("Move to element success")
        self.get_agree_checkbox().click()
        print('Click agree_checkbox')

    def input_agree_checkbox_text(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.agree_checkbox_text)))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        print("Move to element success")
        self.get_agree_checkbox_text().click()
        print('Click agree_checkbox_text')

    def input_begin_talk_button(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.begin_talk_button)))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        print("Move to element success")
        self.get_begin_talk_button().click()
        print('Click begin_talk_button')

    def click_close_window_ask_questions(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.close_window_ask_questions)))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        print("Move to element success")
        self.get_close_window_ask_questions().click()
        print('Click close_window_ask_questions')



    # Actions

    def subheadings_menu_elements_right_online_consultant(self):
        with allure.step('subheadings_menu_elements_right_online_consultant'):
            Logger.add_start_step(method='subheadings_menu_elements_right_online_consultant')

            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.get_screenshot()
            print('-' * 100)

            self.click_icon_questions()
            self.get_screenshot()
            print('-' * 100)

            self.click_ask_questions()
            self.get_screenshot()
            self.assert_word(self.assert_ask_questions, 'Для начала диалога введите, пожалуйста, свою контактную информацию и вопрос.')
            print('-' * 100)

            self.input_your_name_input()
            self.get_screenshot()
            print('-' * 100)

            self.input_phone_input()
            self.get_screenshot()
            print('-' * 100)

            self.input_mail_input()
            self.get_screenshot()
            print('-' * 100)

            self.input_personal_account_input()
            self.get_screenshot()
            print('-' * 100)

            self.input_message_area()
            self.get_screenshot()
            print('-' * 100)

            self.input_agree_checkbox()
            self.get_screenshot()
            print('-' * 100)

            self.input_agree_checkbox_text()
            print(f"List tabs: {str(self.driver.window_handles)}")
            # time.sleep(3)
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.assert_word(self.assert_agree_checkbox_text, 'Другие документы')
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

            self.get_screenshot()
            print('-' * 100)

            self.input_begin_talk_button()
            self.get_screenshot()
            print('-' * 100)

            self.click_close_window_ask_questions()
            self.get_current_url()
            self.get_screenshot()
            print('-' * 100)






            Logger.add_end_step(url=self.driver.current_url, method='subheadings_menu_elements_right_online_consultant')