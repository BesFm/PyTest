from selenium.webdriver.common.by import By
from generator.generator import generated_person


class FormsPageLocators:

    # Заполнение формы
    INPUT_FIRSTNAME = (By.CSS_SELECTOR, "input[id='firstName']")
    INPUT_LASTNAME = (By.CSS_SELECTOR, "input[id='lastName']")
    INPUT_EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    GENDER_RADIO = ((By.CSS_SELECTOR, "label[for='gender-radio-1']"),
                    (By.CSS_SELECTOR, "label[for='gender-radio-2']"),
                    (By.CSS_SELECTOR, "label[for='gender-radio-3']"))
    MOBILE_NUMBER = (By.CSS_SELECTOR, "input[id='userNumber']")
    DATE_OF_BIRTH = (By.CSS_SELECTOR, "input[id='dateOfBirthInput']")
    SELECT_MONTH = (By.CSS_SELECTOR, "select[class='react-datepicker__month-select'] option")
    SELECT_YEAR = (By.CSS_SELECTOR, "select[class='react-datepicker__year-select'] option")
    SELECT_DAY = (By.CSS_SELECTOR, "div[class^='react-datepicker__day react-datepicker__day--']")
    INPUT_SUBJECTS = (By.CSS_SELECTOR, "input[id='subjectsInput']")
    HOBBIES_CHECKBOX = ((By. CSS_SELECTOR, "label[for='hobbies-checkbox-1']"),
                        (By. CSS_SELECTOR, "label[for='hobbies-checkbox-2']"),
                        (By. CSS_SELECTOR, "label[for='hobbies-checkbox-3']"))
    UPLOAD_PICTURE = (By.CSS_SELECTOR, "input[id='uploadPicture']")
    INPUT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    SELECT_STATE = (By.CSS_SELECTOR, "div[id='state']")
    INPUT_STATE = (By.CSS_SELECTOR, "input[id='react-select-3-input']")
    SELECT_CITY = (By.CSS_SELECTOR, "div[id='city']")
    INPUT_CITY = (By.CSS_SELECTOR, "input[id='react-select-4-input']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[id='submit']")

    # Получение значений
    OUTPUT_INFO = (By.XPATH, "//div[@class='table-responsive']//td[2]")
    CLOSE_TABLE = (By.CSS_SELECTOR, "button[id='closeLargeModal']")
