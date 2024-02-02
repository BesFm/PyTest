from selenium.webdriver.common.by import By


class AccordianPageLocators:

    WHATISLOREMIPSUM_ACCORD = (By.CSS_SELECTOR, "div[id='section1Heading']")
    WHATDOESITCOMEFROM_ACCORD = (By.CSS_SELECTOR, "div[id='section2Heading']")
    WHYDOWEUSEIT_ACCORD = (By.CSS_SELECTOR, "div[id='section3Heading']")

    WHATISLOREMIPSUM_TEXT = (By.CSS_SELECTOR, "div[id='section1Content'] p")
    WHATDOESITCOMEFROM_TEXT = (By.CSS_SELECTOR, "div[id='section2Content'] p")
    WHYDOWEUSEIT_TEXT = (By.CSS_SELECTOR, "div[id='section3Content'] p")


class AutoCompletePageLocators:

    MULTIPLE_COLOR_INPUT = (By.CSS_SELECTOR, "input[id='autoCompleteMultipleInput']")
    SINGLE_COLOR_INPUT = (By.CSS_SELECTOR, "input[id='autoCompleteSingleInput']")
    MULTI_INPUT_RESULT = (By.CSS_SELECTOR, "div[class='css-1rhbuit-multiValue auto-complete__multi-value']")
    SINGLE_INPUT_RESULT = (By.CSS_SELECTOR, "div[class='auto-complete__single-value css-1uccc91-singleValue']")
    DELETE_ONE_COLOR = (By.CSS_SELECTOR, "svg[class='css-19bqh2r'][height='14']")
    DELETE_ALL_COLORS = (By.CSS_SELECTOR, "svg[class='css-19bqh2r'][height='20']")


class DatePickerPageLocators:

    INPUT_DATE = (By.CSS_SELECTOR, "input[id='datePickerMonthYearInput']")
    SELECT_MONTH = (By.CSS_SELECTOR, "select[class='react-datepicker__month-select']")
    SELECT_YEAR = (By.CSS_SELECTOR, "select[class='react-datepicker__year-select']")
    SELECT_DAY = (By.CSS_SELECTOR, "div[class^='react-datepicker__day react-datepicker__day']")

    TIME_DATE_INPUT = (By.CSS_SELECTOR, "input[id='dateAndTimePickerInput']")
    TIME_DATE_MONTH_DROP = (By.CSS_SELECTOR, "span[class='react-datepicker__month-read-view--down-arrow']")
    TIME_DATE_SELECT_MONTH = (By.CSS_SELECTOR, "div[class='react-datepicker__month-option']")
    TIME_DATE_YEAR_DROP = (By.CSS_SELECTOR, "span[class='react-datepicker__year-read-view--down-arrow']")
    TIME_DATE_YEAR_SEARCH_OLD = (By.CSS_SELECTOR, "a[class='react-datepicker__navigation react-datepicker__navigation"
                                                  "--years react-datepicker__navigation--years-previous']")
    TIME_DATE_YEAR_SEARCH_NEW = (By.CSS_SELECTOR, "a[class='react-datepicker__navigation react-datepicker__navigation"
                                                  "--years react-datepicker__navigation--years-upcoming']")
    TIME_DATE_SELECT_YEAR = (By.CSS_SELECTOR, "div[class='react-datepicker__year-option']")
    TIME_DATE_SELECT_TIME = (By.CSS_SELECTOR, "li[class='react-datepicker__time-list-item ']")
