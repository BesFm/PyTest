import time

import allure

from pages.forms_page import FormsPage
from conftest import driver
import os


@allure.suite("TestForms")
class TestForms:
    @allure.title("Test all from")
    def test_all_form(self, driver):
        forms_page = FormsPage(driver, "https://demoqa.com/automation-practice-form")
        forms_page.open()
        forms_page.remove_banners()
        assert forms_page.send_input_info() == forms_page.get_output_info(), "Invalid info"
