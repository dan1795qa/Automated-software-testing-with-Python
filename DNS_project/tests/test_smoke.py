import allure
from selenium import webdriver
from  selenium.webdriver.chrome.options import Options
from pages.additional_product_cart_page import Additional_product_cart_page
from pages.cart_page import Cart_page
from pages.checkout_page import Checkout_page
from pages.main_page import Main_page
from pages.search_list_page import Search_list_page



@allure.epic("Test DNS")
class Test_DNS():


    @allure.description("test_smoke")
    def test_smoke(self):

        options = Options()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(executable_path='C:\\Users\\HP PAVILION\\PycharmProjects\\resource\\chromedriver.exe',chrome_options=options)


        si = Main_page(driver)
        si.search_name_item()

        slp = Search_list_page(driver)
        slp.filter_notebook()

        ac = Cart_page(driver)
        ac.action_cart()

        apap = Additional_product_cart_page(driver)
        apap.action_additional_product_cart()

        cp = Checkout_page(driver)
        cp.checkout()

        driver.quit()