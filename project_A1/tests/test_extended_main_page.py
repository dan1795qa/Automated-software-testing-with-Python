import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from blocks.headers_block import Headers_blocks
from blocks.subheadings_left import Subheadings_left
from blocks.subteadings_right import Subheadings_right


@allure.description("Test 'Headers_menu_elements'")
def test_headers_menu_elements(set_up, set_group):

    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path = 'C:\\Users\\HP PAVILION\\PycharmProjects\\resource\\chromedriver.exe', chrome_options=options)

    print('-' * 100)
    print("Start test 'Headers_menu_elements'")
    hb = Headers_blocks(driver)
    hb.headers_menu_elements()
    print("Finish test 'Headers_menu_elements'")
    print('-' * 100)
#
#
@allure.description("Test 'Subheadings_menu_elements_left'")
def test_subheadings_menu_elements_left (set_up, set_group):

    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='C:\\Users\\HP PAVILION\\PycharmProjects\\resource\\chromedriver.exe',chrome_options=options)

    print('-' * 100)
    print("Start test 'Subheadings_menu_elements_left'")
    print('-' * 100)
    sbh_l = Subheadings_left(driver)
    sbh_l.subheadings_menu_elements_left()
    print("Finish test 'Subheadings_menu_elements_left'")
    print('-' * 100)

@allure.description("Test 'Subheadings_menu_elements_right'")
def test_subheadings_menu_elements_right (set_up, set_group):

    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='C:\\Users\\HP PAVILION\\PycharmProjects\\resource\\chromedriver.exe',chrome_options=options)

    print('-' * 100)
    print("Start test 'Subheadings_menu_elements_right'")
    print('-' * 100)
    sbh_r = Subheadings_right(driver)
    sbh_r.subheadings_menu_elements_right()
    print("Finish test 'Subheadings_menu_elements_right'")
    print('-' * 100)