import pytest
from selenium import webdriver
from data.links import MAIN_PAGE
from pages.main_page import MainPage
from pages.order_page import OrderPage
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Firefox(options=options)
    driver.get(MAIN_PAGE)
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    main_page = MainPage(driver)
    main_page.open_url(MAIN_PAGE)
    main_page.accept_cookies()
    return main_page


@pytest.fixture
def order_page(driver):
    order_page = OrderPage(driver)
    return order_page
