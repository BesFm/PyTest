import time
from pages.base_page import BasePage
from conftest import driver

def test(driver):
    page = BasePage(driver, "https://www.google.com")
    page.open()
    time.sleep(5)
