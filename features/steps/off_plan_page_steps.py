from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Open the main page')
def open_main(context):
    context.app.main_page.open_main()


@then('Input {email} and {password} to Log in to the page')
def valid_credentials(context, email, password):
    sleep(3)
    context.app.off_plan_page.valid_credentials(email, password)


@then('Click on “off plan” at the left side menu')
def click_off_plan(context):
    context.app.off_plan_page.click_off_plan()


@then('Verify the right page opens')
def verify_right_page_opens(context):
    context.app.off_plan_page.verify_right_page_opens()
    sleep(4)


@then('Click the Filters button in the top right corner')
def click_filter_button(context):
    context.app.off_plan_page.click_filter_button()
    sleep(4)


@then('Filter the products by price range from {1200000} to {2000000} AED')
def filter_by_price(context, low_amount, high_amount):
    sleep(3)
    context.app.off_plan_page.filter_by_price(low_amount, high_amount)
    sleep(3)


@then('Verify the price in all cards is inside the range ({min_price} - {max_price})')
def verify_prices_in_range(context, min_price, max_price):
    context.app.off_plan_page.verify_prices_in_range(min_price, max_price)




