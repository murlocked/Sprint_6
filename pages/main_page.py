import allure
import locators.main_page_locators as loc
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.title('Нажать на кнопку «Заказать» вверху страницы')
    def press_order_button_top(self):
        self.click_on_element(loc.BUTTON_ORDER_TOP)

    @allure.title('Нажать на кнопку «Заказать» внизу страницы')
    def press_order_button_bottom(self):
        self.click_on_element(loc.BUTTON_ORDER_BOTTOM)

    @allure.step('Прокрутить страницу до вопросов о важном')
    def scroll_down_to_questions(self):
        self.scroll_down()





