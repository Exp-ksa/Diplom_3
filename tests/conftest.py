import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from data_url import Url
from data import Credentials
from locators.login_locator import LoginLocators
from locators.main_page_locator import MainLocators
from pages.header_menu_page import NavigationMenu
from pages.main_page import MainPage
from pages.order_feed_page import OrderPage


def pytest_generate_tests(metafunc):
    
    if "browser_name" in metafunc.fixturenames:
        metafunc.parametrize("browser_name", ["chrome", "firefox"], scope="function")


@pytest.fixture
def driver(browser_name):  
    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-notifications")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        driver = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        options.set_preference("dom.webdriver.enabled", False)
        options.set_preference("useAutomationExtension", False)
        options.set_preference("dom.push.enabled", False)
        driver = webdriver.Firefox(options=options)

    else:
        raise ValueError(f"Неподдерживаемый браузер: {browser_name}")

    driver.implicitly_wait(5)

    yield driver

    driver.quit()

@pytest.fixture(scope="function")
def main_page(driver):
    driver.get(Url.BASE_URL)
    return MainPage(driver)

@pytest.fixture(scope="function")
def order_feed_page(driver):
    driver.get(Url.ORDER_FEED_URL)
    return OrderPage(driver)

@pytest.fixture(scope="function")
def navigation_menu(driver):
    driver.get(Url.LOGIN_URL)
    return NavigationMenu(driver)

@pytest.fixture(scope="function")
def authorization_main_page(main_page):
    main_page.click_element_js(MainLocators.LOGIN_BUTTON)
    
    main_page.send_keys_to_element(LoginLocators.EMAIL_FIELD, Credentials.email)
    main_page.send_keys_to_element(LoginLocators.PASSWORD_FIELD, Credentials.password)
    main_page.click_element_js(LoginLocators.LOGIN_BUTTON)

    main_page.wait_for_element_visible(MainLocators.ORDER_BUTTON)

    return main_page
