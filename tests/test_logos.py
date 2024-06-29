import allure
from data.links import DZEN_REDIRECT_PAGE
import locators.main_page_locators as loc


class TestYandexLogoRedirection:

    @allure.title('Проверка перенаправления на страницу Дзен')
    def test_click_yandex_logo(self, main_page):
        main_page.click_on_element(loc.YANDEX_LOGO)
        main_page.wait_for_redirect(DZEN_REDIRECT_PAGE)
        assert main_page.get_current_url == DZEN_REDIRECT_PAGE


class TestScooterLogoRedirection:

    @allure.title('Проверка перенаправления на страницу Самоката')
    def test_click_scooter_logo(self, main_page):
        main_page.click_on_element(loc.SCOOTER_LOGO)
        assert not 'order' in main_page.get_current_url
