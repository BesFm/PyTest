from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:

    NEW_TAB_BUTTON = (By.CSS_SELECTOR, "button[id='tabButton']")
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, "button[id='windowButton']")
    RESPONSE_TITLE = (By.CSS_SELECTOR, "h1[id='sampleHeading']")


class AlertsPageLocators:

    SIMPLE_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='alertButton']")
    TIME_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='timerAlertButton']")
    CONFIRM_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='confirmButton']")
    PROMPT_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='promtButton']")
    CONFIRM_RESULT = (By.CSS_SELECTOR, "span[id='confirmResult']")
    PROMPT_RESULT = (By.CSS_SELECTOR, "span[id='promptResult']")


class FramePageLocators:

    FIRST_FRAME = (By.CSS_SELECTOR, "iframe[id='frame1']")
    SECOND_FRAME = (By.CSS_SELECTOR, "iframe[id='frame2']")
    RESPONSE_FRAME = (By.CSS_SELECTOR, "h1[id='sampleHeading']")


class NestedFramesLocators:

    LARGE_FRAME = (By.CSS_SELECTOR, "iframe[id='frame1']")
    SMALL_FRAME = (By.CSS_SELECTOR, "iframe[srcdoc='<p>Child Iframe</p>']")
    LFRAME_TEXT = (By.XPATH, "//*[contains(text(),'Parent frame')]")
    SFRAME_TEXT = (By.XPATH, "//*[contains(text(),'Child Iframe')]")
