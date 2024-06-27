import allure
import locators.main_page_locators as loc
from pages.main_page import MainPage


class TestYandexLogoRedirection:

    @allure.title('Проверка перенаправления на страницу Дзен')
    def test_click_yandex_logo(self, driver):
        page = MainPage(driver)
        page.click_on_element(loc.YANDEX_LOGO)
        assert not len(driver.window_handles) == 1


class TestScooterLogoRedirection:

    @allure.title('Проверка перенаправления на страницу Самоката')
    def test_click_scooter_logo(self, driver):
        page = MainPage(driver)
        page.click_on_element(loc.SCOOTER_LOGO)
        assert not 'order' in driver.current_url
