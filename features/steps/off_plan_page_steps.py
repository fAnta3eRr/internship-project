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
    context.app.off_plan_page.valid_credentials(email, password)


@then('Click on {locator} at the left side menu')
def click_header_locator(context, locator):
    context.app.off_plan_page.click_header_locator(locator)


@then('Verify the right page opens')
def verify_right_page_opens(context):
    context.app.off_plan_page.verify_right_page_opens()


@then('Verify the right page opens in mobile')
def verify_right_page_opens(context):
    context.app.off_plan_page.verify_right_page_opens_mobile()


@then('Click the Filters button in the top right corner')
def click_filter_button(context):
    context.app.off_plan_page.click_filter_button()


@then('Click the Filters button in the top right corner in mobile')
def click_filter_button_mobile(context):
    context.app.off_plan_page.click_filter_button_mobile()


@then('Filter the products by price range from {low_amount} to {high_amount} AED')
def filter_by_price(context, low_amount, high_amount):
    context.app.off_plan_page.filter_by_price(low_amount, high_amount)
    sleep(4)


@then('Verify the price in all cards is inside the range ({min_price} - {max_price})')
def verify_prices_in_range(context, min_price, max_price):
    context.app.off_plan_page.verify_prices_in_range(min_price, max_price)




