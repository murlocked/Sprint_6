import allure
import pytest
from data.parameters import faq_params


class TestQuestions:

    @allure.title('Проверка выпадающего списка')
    @pytest.mark.parametrize('question_id, expected_reply, reply_text', faq_params)
    def test_click_on_questions(self, main_page, question_id, expected_reply, reply_text):
        main_page.scroll_down_to_questions()
        main_page.click_on_element(question_id)
        main_page.find_element(expected_reply)
        assert reply_text in main_page.find_text(expected_reply)
