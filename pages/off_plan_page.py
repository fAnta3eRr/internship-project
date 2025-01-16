from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class OffPlanPage(BasePage):


    EMAIL_FILED = (By.CSS_SELECTOR, "[type='email']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "[data-name='Password']")
    OFF_PLAN_BUTTON = (By.CSS_SELECTOR, "[class*='1-link-menu']")
    RIGHT_PAGE = (By.XPATH, "//div[text()= 'Total projects']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[wized='loginButton']")
    APPLY_FILTER_BUTTON = (By.CSS_SELECTOR, "[wized='applyFilterButton']")
    MIN_PRICE_FIELD = (By.XPATH, "//div/div[1]//input[@id='field-5']")
    MAX_PRICE_FILED = (By.XPATH, "//div[2]/input[@id='field-5']")
    PRODUCT_PRICE = (By.CSS_SELECTOR,  "[class='price-value']")
    PRODUCT_CARDS = (By.CSS_SELECTOR, "[wized='cardOfProperty']")
    FILTER_BUTTON = (By.XPATH, "//a[@wized='openFiltersWindow']//div[@class='filter-text']")


    def valid_credentials(self, username, password):
        self.input_text(username, *self.EMAIL_FILED)
        self.input_text(password, *self.PASSWORD_FIELD)
        self.wait_and_click(*self.CONTINUE_BUTTON)


    def click_off_plan(self):
        self.wait_and_click(*self.OFF_PLAN_BUTTON)


    def verify_right_page_opens(self):
        self.verify_text('Total projects', *self.RIGHT_PAGE)


    def click_filter_button(self):
        self.wait_and_click(*self.FILTER_BUTTON)


    def filter_by_price(self, low_price, high_price):
        self.input_text(low_price, *self.MIN_PRICE_FIELD)
        self.input_text(high_price, *self.MAX_PRICE_FILED)
        self.wait_and_click(*self.APPLY_FILTER_BUTTON)


    def verify_prices_in_range(self, low_price, high_price):
        invalid_prices = []

        for card in self.find_elements(*self.PRODUCT_CARDS):
            try:
                price_text = card.find_element(*self.PRODUCT_PRICE).text
                price = int(price_text.replace("AED", "").replace(",", "").strip())

                if not (int(low_price) <= int(price) <= int(high_price)):
                    invalid_prices.append(f"Price {price} is out of range in card: {card}")
            except NoSuchElementException:
                invalid_prices.append(f'Missing or invalid price in card: {card}')

        assert not invalid_prices, f"Found invalid prices: {invalid_prices}"



















