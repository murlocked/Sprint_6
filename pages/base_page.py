from typing import Any
from dataclasses import dataclass
import locators.main_page_locators as loc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@dataclass
class BasePage:

    driver: Any

    @staticmethod
    def open_url(driver, url):
        driver.get(url)

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
