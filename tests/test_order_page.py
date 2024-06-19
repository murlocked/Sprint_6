import allure
from pages.order_page import OrderPage
import data.users as usr
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import data.locators as loc


class TestOrderPage:
    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.add_argument("--window-size=1920,1080")
        cls.driver = webdriver.Firefox(options=options)
        cls.driver.get('https://qa-scooter.praktikum-services.ru/order')
        cls.order_page = OrderPage(cls.driver)

    @allure.title('Проверка оформления заказа')
    @allure.description('Проверка позитивного сценария заказа самоката')
    def test_make_order_positive(self):
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(loc.ACCEPT_COOKIES)).click()
        self.order_page.fill_in_name_field(usr.NAMES[0])
        self.order_page.fill_in_last_name_field(usr.LAST_NAMES[0])
        self.order_page.fill_in_address_field(usr.ADDRESSES[0])
        self.order_page.fill_in_metro_station_field(usr.STATIONS[0])
        self.order_page.fill_in_telephone_number_field(usr.TELEPHONE_NUMBERS[0])
        self.order_page.click_on_button_next()

        self.order_page.set_delivery_date()
        self.order_page.click_on_time_of_lease_field()
        self.order_page.choose_scooter_color()

        self.order_page.fill_in_comment_field('comment')
        self.order_page.click_order_button()
        self.order_page.click_yes_button()
        self.driver.find_element(*loc.SHOW_STATUS_BUTTON).click()

        assert 'track' in self.driver.current_url

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
