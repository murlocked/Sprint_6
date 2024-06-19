import allure
from typing import Any
from dataclasses import dataclass

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import data.locators as loc


@dataclass
class OrderPage:
    driver: Any

    @allure.step('Заполнить поле Имя')
    def fill_in_name_field(self, data):
        self.driver.find_element(*loc.NAME_FIELD).send_keys(data)

    @allure.step('Заполнить поле Фамилия')
    def fill_in_last_name_field(self, data):
        self.driver.find_element(*loc.LAST_NAME_FIELD).send_keys(data)

    @allure.step('Заполнить поле Адрес')
    def fill_in_address_field(self, data):
        self.driver.find_element(*loc.ADDRESS_FIELD).send_keys(data)

    @allure.step('Заполнить поле Станция метро')
    def fill_in_metro_station_field(self, data):
        self.driver.find_element(*loc.METRO_STATION_FIELD).click()
        station = [By.XPATH, fr'//*[contains(text(), "{data}")]']
        self.driver.find_element(*station).click()

    @allure.step('Заполнить поле Телефон')
    def fill_in_telephone_number_field(self, data):
        self.driver.find_element(*loc.TELEPHONE_NUMBER_FIELD).send_keys(data)

    @allure.step('Нажать кнопку Далее')
    def click_on_button_next(self):
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(loc.BUTTON_NEXT)).click()

    @allure.step('Выбрать дату доставки')
    def set_delivery_date(self):
        self.driver.find_element(*loc.WHEN_BRING_SCOOTER_FIELD).click()
        self.driver.find_element(*loc.DATE_CALENDAR).click()

    @allure.step('Выбрать длительность аренды')
    def click_on_time_of_lease_field(self):
        self.driver.find_element(*loc.LEASE_TERM_FIELD).click()
        self.driver.find_element(*loc.RENTAL_PERIOD_ONE_DAY).click()

    @allure.step('Выбрать цвет самоката')
    def choose_scooter_color(self):
        self.driver.find_element(*loc.SCOOTER_COLOR).click()

    @allure.step('Добавить комментарий')
    def fill_in_comment_field(self, text):
        self.driver.find_element(*loc.COMMENT_FIELD).click()
        self.driver.find_element(*loc.COMMENT_FIELD).send_keys(text)

    @allure.step('Нажать кнопку Заказать')
    def click_order_button(self):
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(loc.ORDER_BUTTON)).click()

    @allure.step('Нажать кнопку подтверждения')
    def click_yes_button(self):
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(loc.ORDER_CONFIRMATION_BUTTON)).click()

    @allure.step('Найти на странице окно с подтверждением')
    def find_status_button(self):
        self.driver.find_element(*loc.SHOW_STATUS_BUTTON)
