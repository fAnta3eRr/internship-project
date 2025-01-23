from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class GoogleSearchPage(BasePage):


    SEARCH_INPUT = (By.CSS_SELECTOR, "[name='q']")
    SEARCH_SUBMIT = (By.CSS_SELECTOR, "[name='btnK']")


    def open_main(self):
        self.open_url('https://www.google.com/')

    def input_search(self, product_name):
        self.input_text(product_name, *self.SEARCH_INPUT)

    def click_search_icon(self):
        self.wait_and_click(*self.SEARCH_SUBMIT)

    def verify_found_results_text(self, product_name):
        result = self.verify_text(product_name, *self.SEARCH_INPUT)
        assert 'Car' in result, F'Expected "{product_name}",but got "{result}"'