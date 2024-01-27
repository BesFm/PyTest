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
    SELECT_MONTH = (By.CSS_SELECTOR, "select[class='react-datepicker__month-select']")
    SP = next(generated_person()).birth_date
    MONTH_OF_BIRTH = (By.CSS_SELECTOR, f"option[value='{int(SP[1])}']")
    SELECT_YEAR = (By.CSS_SELECTOR, "select[class='react-datepicker__year-select']")
    YEAR_OF_BIRTH = (By.CSS_SELECTOR, f"option[value='{SP[0]}']")
    SELECT_DAY = (By.XPATH, f"//div[@class='react-datepicker__month']//*[contains(text(),"
                            f" {SP[2]})]")
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
