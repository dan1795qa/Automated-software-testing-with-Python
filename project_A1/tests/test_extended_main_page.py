from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from blocks.headers_block import Headers_blocks
from blocks.subheadings import Subteadings


def test_extended_main_page():

    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path = 'C:\\Users\\HP PAVILION\\PycharmProjects\\resource\\chromedriver.exe', chrome_options=options)

    print("Start test regress main page")

    print('-' * 100)
    print("Start test 'Headers_menu_elements'")
    hb = Headers_blocks(driver)
    hb.headers_menu_elements()
    print("Finish test 'Headers_menu_elements'")
    print('-' * 100)

    print('-' * 100)
    print("Start test 'Subheadings_menu_elements'")
    sbh = Subteadings(driver)
    sbh.subheadings_menu_elements()
    print("Finish test'Subheadings_menu_elements'")
    print('-' * 100)

