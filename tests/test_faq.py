import pytest
import allure
from tests.data import Answers
from pages.home_page import HomePage


class TestFaq:

    @allure.title("FAQ answers")
    @allure.description("Проверка корректности ответов на вопросы")
    @pytest.mark.parametrize("question_locator, answer_locator, expected_answer_text", Answers.test_data)
    def test_question_answer(self, driver, question_locator, answer_locator, expected_answer_text):
        home_page = HomePage(driver)
        answer_text = home_page.get_answer_text(question_locator, answer_locator)
        assert answer_text == expected_answer_text, f"Failed to compare the answer text for {question_locator}"
