from selenium.webdriver.common.by import By

# buttons
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

# other
DATE_CALENDAR = [By.XPATH, './/div[@class="react-datepicker__day react-datepicker__day--010"]']
RENTAL_PERIOD_ONE_DAY = [By.XPATH, "//div[@class='Dropdown-menu']/div['сутки']"]
SCOOTER_COLOR = [By.XPATH, './/label[text() = "чёрный жемчуг"]']


def metro_station_dynamic(station_name):
    return [By.XPATH, fr'//*[contains(text(), "{station_name}")]']
