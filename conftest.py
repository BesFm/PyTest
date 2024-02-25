from datetime import datetime

import allure

import pytest
from selenium import webdriver
from selenium.common import UnexpectedAlertPresentException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    try:
        attach = driver.get_screenshot_as_png()
        allure.attach(attach, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG)
    except UnexpectedAlertPresentException as UnexAlert:
        print(f"Screenshot hasn't been taken because of {UnexAlert}Error")
    driver.quit()
