from pages.base_page import BasePage
from pages.google_search_page import GoogleSearchPage
from pages.main_page import MainPage
from pages.off_plan_page import OffPlanPage


class Application:
    def __init__(self, driver):
        self.driver = driver

        self.base_page = BasePage(driver)
        self.main_page = MainPage(driver)
        self.google_search_page = GoogleSearchPage(driver)
        self.off_plan_page  = OffPlanPage(driver)