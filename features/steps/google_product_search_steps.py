from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@given('Open Google page')
def open_google(context):
    context.app.google_search_page.open_main()


@when('Input {search_word} into search field')
def input_search(context, search_word):
    (context.app.google_search_page.input_search(search_word))


@when('Click on search icon')
def click_search_icon(context):
    context.app.google_search_page.click_search_icon()


@then('Product results for {product_name} are shown')
def verify_found_results_text(context, product_name):
    context.app.google_search_page.verify_found_results_text(product_name)
