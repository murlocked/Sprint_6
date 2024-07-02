import allure
import pytest
from data.parameters import order_user_data


class TestOrderPage:

    @pytest.mark.parametrize('name, last_name, address, metro_station, mobile_number, start_button',
                             order_user_data)
    @allure.title('Проверка оформления заказа')
    @allure.description('Проверка позитивного сценария заказа самоката')
    def test_make_order_positive(self, main_page, order_page, name,
                                 last_name, address,
                                 metro_station, mobile_number, start_button):
        main_page.click_on_element(start_button)

        order_page.fill_in_order_first_page(name, last_name, address, metro_station, mobile_number)
        order_page.click_on_button_next()
        order_page.fill_in_order_second_page()
        order_page.click_order_button()
        order_page.confirm_order()

        assert 'track' in main_page.get_current_url
