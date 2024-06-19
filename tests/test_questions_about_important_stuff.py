import allure
from pages.main_page import MainPage
from data.questions import answers
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import data.locators as loc


class TestQuestions:
    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.add_argument("--window-size=1920,1080")
        cls.driver = webdriver.Firefox(options=options)
        cls.driver.get('https://qa-scooter.praktikum-services.ru')
        cls.main_page = MainPage(cls.driver).scroll_down()
        WebDriverWait(cls.driver, 20).until(ec.element_to_be_clickable(loc.ACCEPT_COOKIES)).click()

    @allure.title('Проверка выпадающего списка: «Сколько это стоит? И как оплатить?»')
    def test_faq_how_much(self):
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(loc.QUESTION_HOW_MUCH)).click()
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(loc.ANSWER_HOW_MUCH))
        assert answers[0] in self.driver.find_element(*loc.ANSWER_HOW_MUCH).text

    @allure.title('Проверка выпадающего списка: «Хочу сразу несколько самокатов! Так можно?»')
    def test_faq_several(self):
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(loc.QUESTION_SEVERAL)).click()
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(loc.ANSWER_SEVERAL))
        assert answers[1] in self.driver.find_element(*loc.ANSWER_SEVERAL).text

    @allure.title('Проверка выпадающего списка: «Как рассчитывается время аренды?»')
    def test_faq_time(self):
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(loc.QUESTION_TIME)).click()
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(loc.ANSWER_TIME))
        assert answers[2] in self.driver.find_element(*loc.ANSWER_TIME).text

    @allure.title('Проверка выпадающего списка: «Можно ли заказать самокат прямо на сегодня?»')
    def test_faq_today_order(self):
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(loc.QUESTION_TODAY_ORDER)).click()
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(loc.ANSWER_TODAY_ORDER))
        assert answers[3] in self.driver.find_element(*loc.ANSWER_TODAY_ORDER).text

    @allure.title('Проверка выпадающего списка: «Можно ли продлить заказ или вернуть самокат раньше?»')
    def test_faq_prolong_order(self):
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(loc.QUESTION_PROLONG_ORDER)).click()
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(loc.ANSWER_PROLONG_ORDER))
        assert answers[4] in self.driver.find_element(*loc.ANSWER_PROLONG_ORDER).text

    @allure.title('Проверка выпадающего списка: «Вы привозите зарядку вместе с самокатом?»')
    def test_faq_charger(self):
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(loc.QUESTION_CHARGER)).click()
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(loc.ANSWER_CHARGER))
        assert answers[5] in self.driver.find_element(*loc.ANSWER_CHARGER).text

    @allure.title('Проверка выпадающего списка: «Можно ли отменить заказ?»')
    def test_faq_cancel(self):
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(loc.QUESTION_CANCEL)).click()
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(loc.ANSWER_CANCEL))
        assert answers[6] in self.driver.find_element(*loc.ANSWER_CANCEL).text

    @allure.title('Проверка выпадающего списка: «Я жизу за МКАДом, привезёте?»')
    def test_faq_mkad(self):
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(loc.QUESTION_MKAD)).click()
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(loc.ANSWER_MKAD))
        assert answers[7] in self.driver.find_element(*loc.ANSWER_MKAD).text

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
