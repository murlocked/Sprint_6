import allure
from typing import Any
import data.locators as loc
from dataclasses import dataclass
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


@dataclass
class MainPage:
    driver: Any

    @allure.title('Нажать на кнопку «Заказать» вверху страницы')
    def press_order_button_top(self):
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(loc.BUTTON_ORDER_TOP)).click()

    @allure.title('Нажать на кнопку «Заказать» внизу страницы')
    def press_order_button_bottom(self):
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(loc.BUTTON_ORDER_BOTTOM)).click()

    @allure.step('Прокрутить страницу до вопросов о важном')
    def scroll_down(self):
        element = self.driver.find_element(*loc.FAQ)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)





