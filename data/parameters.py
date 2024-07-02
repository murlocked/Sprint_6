from data.questions import answers
import locators.main_page_locators as loc

faq_params = [
    (loc.QUESTION_HOW_MUCH, loc.ANSWER_HOW_MUCH, answers[0]),
    (loc.QUESTION_SEVERAL, loc.ANSWER_SEVERAL, answers[1]),
    (loc.QUESTION_TIME, loc.ANSWER_TIME, answers[2]),
    (loc.QUESTION_TODAY_ORDER, loc.ANSWER_TODAY_ORDER, answers[3]),
    (loc.QUESTION_PROLONG_ORDER, loc.ANSWER_PROLONG_ORDER, answers[4]),
    (loc.QUESTION_CHARGER, loc.ANSWER_CHARGER, answers[5]),
    (loc.QUESTION_CANCEL, loc.ANSWER_CANCEL, answers[6]),
    (loc.QUESTION_MKAD, loc.ANSWER_MKAD, answers[7])
]

order_user_data = [
    ('Иван', 'Иванов', 'Тверская улица 11', 'Бульвар Рокоссовского', '+79269876543', loc.BUTTON_ORDER_TOP),
    ('Юлия', 'Морозова', 'Таврический 5', 'Сокольники', '+79269878965', loc.BUTTON_ORDER_BOTTOM)
]
