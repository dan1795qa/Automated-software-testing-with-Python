import time

import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from pages.gudzon_cart_page import Gudzon_cart_page
from pages.gudzon_product_page import Gudzon_product_page
from pages.main_page import Main_page
from pages.market_search_page import Market_search_page
from pages.product_page import Product_page




@allure.description("test_product")
def test_order_product(set_up):

    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='C:\\Users\\HP PAVILION\\PycharmProjects\\resource\\chromedriver.exe', chrome_options=options)


    services = Main_page(driver)
    services.go_to_market()
    # time.sleep(1)

    mp = Market_search_page(driver)
    mp.search_product()

    pp = Product_page(driver)
    pp.go_to_store()


    gpp = Gudzon_product_page(driver)
    gpp.go_to_cart()

    gcp = Gudzon_cart_page(driver)
    gcp.orderring()

    driver.quit()

