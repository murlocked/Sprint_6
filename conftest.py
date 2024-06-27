import pytest
from selenium import webdriver
from data.links import MAIN_PAGE
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Firefox(options=options)
    driver.get(MAIN_PAGE)
    yield driver
    driver.quit()
