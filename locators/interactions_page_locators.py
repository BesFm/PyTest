from selenium.webdriver.common.by import By


class SortablePageLocators:

    GRID_TAB = (By.CSS_SELECTOR, "a[id='demo-tab-grid']")
    GRID_ELEMENTS = (By.CSS_SELECTOR, "div[class='create-grid'] div")
    LIST_TAB = (By.CSS_SELECTOR, "a[id='demo-tab-list']")
    LIST_ELEMENTS = (By.CSS_SELECTOR, "div[class='vertical-list-container mt-4'] div")
