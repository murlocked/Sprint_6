from typing import Any
from dataclasses import dataclass
import locators.main_page_locators as loc
from locators.main_page_locators import ACCEPT_COOKIES
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@dataclass
class BasePage:

    driver: Any

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, elem):
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(elem))

    def find_text(self, elem):
        return self.driver.find_element(*elem).text

    def enter_text(self, elem, text):
        self.driver.find_element(*elem).send_keys(text)

    def click_on_element(self, elem):
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(elem)).click()

    def scroll_down(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*loc.FAQ))

    def accept_cookies(self):
        self.click_on_element(ACCEPT_COOKIES)

    def wait_for_redirect(self, url):
        WebDriverWait(self.driver, 10).until(ec.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 10).until(lambda driver: driver.current_url == url)

    @property
    def get_current_url(self):
        return self.driver.current_url
