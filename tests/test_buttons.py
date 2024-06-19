import allure
from selenium import webdriver
import data.locators as loc
from pages.main_page import MainPage
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class TestOrderButtonTop:
    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.add_argument("--window-size=1920,1080")
        cls.driver = webdriver.Firefox(options=options)
        cls.driver.get('https://qa-scooter.praktikum-services.ru')
        cls.main_page = MainPage(cls.driver)

    @allure.title('Проверка нажатия на кнопку «Заказать» вверху страницы')
    def test_order_button_top(self):
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(loc.ACCEPT_COOKIES)).click()
        self.main_page.press_order_button_top()
        assert 'order' in self.driver.current_url

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()


class TestOrderButtonBottom:
    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.add_argument("--window-size=1920,1080")
        cls.driver = webdriver.Firefox(options=options)
        cls.driver.get('https://qa-scooter.praktikum-services.ru')
        cls.main_page = MainPage(cls.driver)

    @allure.title('Проверка нажатия на кнопку «Заказать» внизу страницы')
    def test_order_button_bottom(self):
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(loc.ACCEPT_COOKIES)).click()
        self.main_page.press_order_button_top()
        assert 'order' in self.driver.current_url

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
