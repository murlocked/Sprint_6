from selenium.webdriver.common.by import By

# buttons
BUTTON_ORDER_TOP = [By.XPATH, "//button[@class='Button_Button__ra12g']"]
BUTTON_ORDER_BOTTOM = [By.CSS_SELECTOR, ".Button_UltraBig__UU3Lp"]
BUTTON_NEXT = [By.XPATH, '//*[contains(text(), "Далее")]']
ORDER_BUTTON = [By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]
ORDER_CONFIRMATION_BUTTON = [By.XPATH, '//button[.="Да"]']
SHOW_STATUS_BUTTON = [By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text() = "Посмотреть статус"]']

# fields
NAME_FIELD = [By.CSS_SELECTOR, "[placeholder='* Имя']"]
LAST_NAME_FIELD = [By.CSS_SELECTOR, "[placeholder='* Фамилия']"]
ADDRESS_FIELD = [By.CSS_SELECTOR, "[placeholder='* Адрес: куда привезти заказ']"]
METRO_STATION_FIELD = [By.CSS_SELECTOR, "[placeholder='* Станция метро']"]
TELEPHONE_NUMBER_FIELD = [By.CSS_SELECTOR, "[placeholder='* Телефон: на него позвонит курьер']"]
WHEN_BRING_SCOOTER_FIELD = [By.CSS_SELECTOR, "[placeholder='* Когда привезти самокат']"]
LEASE_TERM_FIELD = [By.CSS_SELECTOR, ".Dropdown-placeholder"]
COMMENT_FIELD = [By.CSS_SELECTOR, "[placeholder='Комментарий для курьера']"]

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

# other
DATE_CALENDAR = [By.XPATH, './/div[@class="react-datepicker__day react-datepicker__day--010"]']
RENTAL_PERIOD_ONE_DAY = [By.XPATH, "//div[@class='Dropdown-menu']/div['сутки']"]
SCOOTER_COLOR = [By.XPATH, './/label[text() = "чёрный жемчуг"]']
ACCEPT_COOKIES = [By.XPATH, "//button[.='да все привыкли']"]