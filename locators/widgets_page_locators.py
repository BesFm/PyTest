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
