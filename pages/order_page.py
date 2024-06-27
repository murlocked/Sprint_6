import allure
import locators.order_page_locators as loc
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Заполнить первую форму заказа')
    def fill_in_order_first_page(self, name, last_name, address, metro_station, mobile_number):
        self.enter_text(loc.NAME_FIELD, name)
        self.enter_text(loc.LAST_NAME_FIELD, last_name)
        self.enter_text(loc.ADDRESS_FIELD, address)
        self.click_on_element(loc.METRO_STATION_FIELD)
        self.click_on_element(loc.metro_station_dynamic(metro_station))
        self.enter_text(loc.TELEPHONE_NUMBER_FIELD, mobile_number)

    @allure.step('Нажать кнопку Далее')
    def click_on_button_next(self):
        self.click_on_element(loc.BUTTON_NEXT)

    @allure.step('Заполнить вторую форму заказа')
    def fill_in_order_second_page(self):
        self.click_on_element(loc.WHEN_BRING_SCOOTER_FIELD)
        self.click_on_element(loc.DATE_CALENDAR)
        self.click_on_element(loc.LEASE_TERM_FIELD)
        self.click_on_element(loc.RENTAL_PERIOD_ONE_DAY)
        self.click_on_element(loc.SCOOTER_COLOR)
        self.enter_text(loc.COMMENT_FIELD, 'comment')

    @allure.step('Нажать кнопку Заказать')
    def click_order_button(self):
        self.click_on_element(loc.ORDER_BUTTON)

    @allure.step('Подтвердить заказ')
    def confirm_order(self):
        self.click_on_element(loc.ORDER_CONFIRMATION_BUTTON)
        self.click_on_element(loc.SHOW_STATUS_BUTTON)
