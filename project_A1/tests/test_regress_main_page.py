from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from blocks.headers_block import Headers_blocks
from blocks.headers_block_proba import Headers_blocks_proba


def test_regress_main_page():

    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path = 'C:\\Users\\HP PAVILION\\PycharmProjects\\resource\\chromedriver.exe', chrome_options=options)

    print("Start test regress main page")

    hb = Headers_blocks(driver)
    hb.headers_menu_elements()

    # hb_proba = Headers_blocks_proba(driver)
    # hb_proba.headers_menu_elements()