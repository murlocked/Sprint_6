import allure
import pytest
import locators.order_page_locators as loc
from locators.main_page_locators import ACCEPT_COOKIES
from data.parameters import order_user_data
from pages.order_page import OrderPage


class TestOrderPage:

    @pytest.mark.parametrize('name, last_name, address, metro_station, mobile_number, start_button',
                             order_user_data)
    @allure.title('Проверка оформления заказа')
    @allure.description('Проверка позитивного сценария заказа самоката')
    def test_make_order_positive(self, driver, name,
                                 last_name, address,
                                 metro_station, mobile_number, start_button):
        page = OrderPage(driver)
        page.click_on_element(ACCEPT_COOKIES)
        page.click_on_element(start_button)

        page.fill_in_order_first_page(name, last_name, address, metro_station, mobile_number)
        page.click_on_button_next()
        page.fill_in_order_second_page()
        page.click_order_button()
        page.confirm_order()

        assert 'track' in driver.current_url
