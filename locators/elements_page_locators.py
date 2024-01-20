from selenium.webdriver.common.by import By



class TextBoxPageLocators:

    #INPUT
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    #OUTPUT
    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")

class CheckBoxPageLocators:
    EXPAND_ALL = (By.CSS_SELECTOR, "button[title='Expand all']")
    COLLAPSE_ALL = (By.CSS_SELECTOR, "button[title='Collapse all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")

    #Проверка
    CHECKED_ELEMENT = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ELEMENT = ".//ancestor::span[@class='rct-text']"
    OUTPUT_CHECKED = (By.CSS_SELECTOR, "span[class='text-success']")


class RadioButtonPageLocators:
    YES_RADIO = (By.CSS_SELECTOR, "label[class^='custom-control-label'][for='yesRadio']")
    IMRESSIVE_RADIO = (By.CSS_SELECTOR, "label[class^='custom-control-label'][for='impressiveRadio']")
    NO_RADIO = (By.CSS_SELECTOR, "label[class^='custom-control-label'][for='noRadio']")

    #Проверка
    CHOOSEN_RADIO = (By.CSS_SELECTOR, "p span[class='text-success']")

class WebTablePageLocators:

    #Ввод значений
    ADD_BUTTON = (By.CSS_SELECTOR, "button[id='addNewRecordButton']")
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, "input[id='firstName']")
    LASTNAME_INPUT = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[id='userEmail']")
    AGE_INPUT = (By.CSS_SELECTOR, "input[id='age']")
    SALARY_INPUT = (By.CSS_SELECTOR, "input[id='salary']")
    DEPARTAMENT_INPUT=(By.CSS_SELECTOR, "input[id='department']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    #Вывод значений
    PERSON_INFO = (By.CSS_SELECTOR, "div[class='rt-tr-group']")

    #Поиск
    SEARCH_FIELD = (By.CSS_SELECTOR, "div input[id='searchBox']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete'")
    ROW_PARENT = ".//ancestor::div[@class='rt-tr -odd']"

    #обновление данных
    UPDATE_BUTTON = (By.CSS_SELECTOR, "span[title='Edit']")

    #проверка удаления
    CHEK_DELETED = (By.CSS_SELECTOR, "div[class='rt-noData']")

    #количество строк
    COUNT_ROW_LIST = (By.CSS_SELECTOR, "select[aria-label='rows per page']")
class ButtonsPageLocators:

    DOUBLE_CLICK_ME = (By.CSS_SELECTOR, "button[id='doubleClickBtn']")
    RIGHT_CLICK_ME = (By.CSS_SELECTOR, "button[id='rightClickBtn']")
    CLICK_ME = (By.XPATH, "//div[3]/button")

    DOUBLE_CLICK_RESULT = (By.CSS_SELECTOR, "p[id='doubleClickMessage']")
    RIGHT_CLICK_RESULT = (By.CSS_SELECTOR, "p[id='rightClickMessage']")
    CLICK_ME_RESULT = (By.CSS_SELECTOR, "p[id='dynamicClickMessage']")

class LinksPageLocators:
    SIMPLE_LINK = (By.CSS_SELECTOR, "a[id='simpleLink']")
    BED_REQUEST_LINK = (By.CSS_SELECTOR, "a[id='bad-request']")
    CREATED_LINK = (By.CSS_SELECTOR, "a[id='created']")
    NO_CONTENT_LINK = (By.CSS_SELECTOR, "a[id='no-content']")
    MOVED_LINK = (By.CSS_SELECTOR, "a[id='moved']")
    UNAUTHORIZED_LINK = (By.CSS_SELECTOR, "a[id='unauthorized']")
    FORBIDDEN_LINK = (By.CSS_SELECTOR, "a[id='forbidden']")
    NOT_FOUND_LINK = (By.CSS_SELECTOR, "a[id='invalid-url']")

class UpDownLoadPageLocators:
    DOWNLOAD_BUTTON = (By.CSS_SELECTOR, "a[id='downloadButton']")
    UPLOAD_BUTTON = (By.CSS_SELECTOR, "input[id='uploadFile']")
    UPLOAD_FILE_PATH = (By.CSS_SELECTOR, "p[id='uploadedFilePath']")

class DynamicPropertiesPageLocators:
    ENABLE_IN_BUTTON = (By.CSS_SELECTOR, "button[id='enableAfter']")
    COLOR_CHANGE_BUTTON = (By.CSS_SELECTOR, "button[id='colorChange']")
    VISIBLE_IN_BUTTON = (By.CSS_SELECTOR, "button[id='visibleAfter']")