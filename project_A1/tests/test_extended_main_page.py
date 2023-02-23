from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from blocks.headers_block import Headers_blocks



def test_extended_main_page():

    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path = 'C:\\Users\\HP PAVILION\\PycharmProjects\\resource\\chromedriver.exe', chrome_options=options)

    print("Start test regress main page")

    hb = Headers_blocks(driver)
    hb.headers_menu_elements()
