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
        firstname, lastname, email, mobile, subjects, address = forms_page.fill_inputs()
        gender = forms_page.click_radio_butt()
        day, month, year = forms_page.set_birth_data()
        hobbies = forms_page.click_all_checkboxes()
        filename = forms_page.upload_file()
        state_city = forms_page.set_state_city()
        forms_page.click_submit_butt()
        os.remove(filename)
        input_info = [f"{firstname} {lastname}", email, gender, str(mobile), f"{day} {month},{year}",
                      subjects, hobbies, filename.split("\\")[-1], address, state_city]
        output_info = forms_page.get_output_info()
        assert input_info == output_info, "Invalid info"
