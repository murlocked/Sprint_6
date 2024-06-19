import allure
from selenium import webdriver
import data.locators as loc
from pages.main_page import MainPage
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class TestYandexLogoRedirection:
    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.add_argument("--window-size=1920,1080")
        cls.driver = webdriver.Firefox(options=options)
        cls.driver.get('https://qa-scooter.praktikum-services.ru')

    @allure.title('Проверка перенаправления на страницу Дзен')
    def test_click_yandex_logo(self):
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(loc.YANDEX_LOGO)).click()
        assert not len(self.driver.window_handles) == 1

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()


class TestScooterLogoRedirection:
    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.add_argument("--window-size=1920,1080")
        cls.driver = webdriver.Firefox(options=options)
        cls.driver.get('https://qa-scooter.praktikum-services.ru/order')

    @allure.title('Проверка перенаправления на страницу Самоката')
    def test_click_scooter_logo(self):
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(loc.SCOOTER_LOGO)).click()
        assert not 'order' in self.driver.current_url

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
