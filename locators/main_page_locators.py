from selenium.webdriver.common.by import By

# buttons
BUTTON_ORDER_TOP = [By.XPATH, ".//div[starts-with(@class, 'Header')]/button[text()='Заказать']"]
BUTTON_ORDER_BOTTOM = [By.XPATH, ".//div[starts-with(@class, 'Home')]/button[text()='Заказать']"]

# logos
SCOOTER_LOGO = [By.CSS_SELECTOR, ".Header_LogoScooter__3lsAR"]
YANDEX_LOGO = [By.CSS_SELECTOR, ".Header_LogoYandex__3TSOI"]

# FAQ
FAQ = [By.XPATH, './/div[text() = "Вопросы о важном"]']
QUESTION_HOW_MUCH = [By.XPATH, './/div[text() = "Сколько это стоит? И как оплатить?"]']
ANSWER_HOW_MUCH = [By.XPATH, './/p[text()="Сутки — 400 рублей. Оплата курьеру — наличными или картой."]']

QUESTION_SEVERAL = [By.XPATH, './/div[@class="accordion__button" and text() = "Хочу сразу несколько самокатов! '
                                             'Так можно?"]']
ANSWER_SEVERAL = [By.XPATH, './/p[text() = "Пока что у нас так: один заказ — один самокат. '
                                           'Если хотите покататься с друзьями, '
                                           'можете просто сделать несколько заказов — один за другим."]']

QUESTION_TIME = [By.XPATH, './/div[@class="accordion__button" and text() = "Как рассчитывается время аренды?" ]']
ANSWER_TIME = [By.XPATH, './/p[text() = "Допустим, вы оформляете заказ на 8 мая. '
                                       'Мы привозим самокат 8 мая в течение дня. '
                                       'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. '
                                       'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."]']

QUESTION_TODAY_ORDER = [By.XPATH, './/div[@class="accordion__button" and text() = "Можно ли заказать самокат прямо на сегодня?"]']
ANSWER_TODAY_ORDER = [By.XPATH, './/p[text() = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."]']

QUESTION_PROLONG_ORDER = [By.XPATH, './/div[@class="accordion__button" and text() = "Можно ли продлить заказ или вернуть самокат раньше?" ]']
ANSWER_PROLONG_ORDER = [By.XPATH, './/p[text() = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."]']

QUESTION_CHARGER = [By.XPATH, './/div[@class="accordion__button" and text() = "Вы привозите зарядку вместе с самокатом?"]']
ANSWER_CHARGER = [By.XPATH, './/p[text() = "Самокат приезжает к вам с полной зарядкой. '
                                              'Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. '
                                              'Зарядка не понадобится."]']

QUESTION_CANCEL = [By.XPATH, './/div[@class="accordion__button" and text() = "Можно ли отменить заказ?"]']
ANSWER_CANCEL = [By.XPATH, './/p[text() = "Да, пока самокат не привезли. '
                                         'Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."]']

QUESTION_MKAD = [By.XPATH, './/div[@class="accordion__button" and text() = "Я жизу за МКАДом, привезёте?"]']
ANSWER_MKAD = [By.XPATH, './/p[text() = "Да, обязательно. Всем самокатов! И Москве, и Московской области."]']

# others
ACCEPT_COOKIES = [By.XPATH, "//button[.='да все привыкли']"]