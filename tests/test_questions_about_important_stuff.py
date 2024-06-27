import allure
import pytest
from locators.main_page_locators import ACCEPT_COOKIES
from data.parameters import faq_params
from pages.main_page import MainPage


class TestQuestions:

    @allure.title('Проверка выпадающего списка')
    @pytest.mark.parametrize('question_id, expected_reply, reply_text', faq_params)
    def test_click_on_questions(self, driver, question_id, expected_reply, reply_text):
        page = MainPage(driver)
        page.click_on_element(ACCEPT_COOKIES)
        page.scroll_down_to_questions()
        page.click_on_element(question_id)
        page.find_element(expected_reply)
        assert reply_text in page.find_text(expected_reply)
