from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.core import driver

from app.application import Application
from webdriver_manager.firefox import GeckoDriverManager


def browser_init(context, scenario_name ):  # BROWSERSTACK add(scenario_name)
    """
    :param context: Behave context
    """
    #Chrome
    #driver_path = ChromeDriverManager().install()
    #service = Service(driver_path)
    #context.driver = webdriver.Chrome(service=service)

    #Mobile emulation (locally)

    # chrome_options = Options()
    # mobile_emulation = {"deviceName": "Pixel 3"}
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    #
    # service = Service(ChromeDriverManager().install())
    # service.start()
    #
    # context.driver = webdriver.Chrome(service=service, options=chrome_options)
    # context.driver.get('http://www.example.com')


    # Firefox
    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)


    ### HEADLESS MODE ####
    #options = webdriver.ChromeOptions()
    #options.add_argument('headless')
    #service = Service(ChromeDriverManager().install())
    #context.driver = webdriver.Chrome(
    #   options=options,
    #   service=service
    #)

    ### BROWSERSTACK ###
    #bs_user = 'yevheniiustenko_S2NqLi'
    #bs_key = 'BkgrTJpGVAJ9qxorVxKX'
    #url = f'http://hub-cloud.browserstack.com/wd/hub'

    #options = Options()
    #bstack_options = {
    #    "os": "Windows",
    #    "osVersion": "11",
    #    "browserName": "Chrome",
    #    "browserVersion": "latest",
    #    'sessionName': scenario_name,
    #}
    #options.set_capability('bstack:options', bstack_options)
    #options.set_capability('browserstack.user', bs_user)
    #options.set_capability('browserstack.key', bs_key)
    #context.driver = webdriver.Remote(command_executor=url, options=options)


    ### BROWSERSTACK ### Mobile
    bs_user = 'yevheniiustenko_S2NqLi'
    bs_key = 'BkgrTJpGVAJ9qxorVxKX'
    url = f'http://hub-cloud.browserstack.com/wd/hub'

    options = Options()
    bstack_options = {
        "deviceName": "Google Pixel 3",
        "os": "Android",
        "osVersion": "9.0",
        "browserName": "Chrome",
        "browserVersion": "latest",
        "deviceOrientation": "portrait",
        "sessionName": scenario_name,
    }

    options.set_capability('bstack:options', bstack_options)
    options.set_capability('browserstack.user', bs_user)
    options.set_capability('browserstack.key', bs_key)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    # context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver,  15)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)    #BROWSERSTACK add(scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()






