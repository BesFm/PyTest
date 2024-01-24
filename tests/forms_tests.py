from pages.forms_page import FormsPage
from conftest import driver
import os


class TestForms:

    def test_all_form(self, driver):
        forms_page = FormsPage(driver, "https://demoqa.com/automation-practice-form")
        forms_page.open()
        forms_page.remove_banners()
        firstname, lastname, email, mobile, subjects, address = forms_page.check_inputs()
        gender = forms_page.check_radio_butt()
        day, month, year = forms_page.check_calendar()
        hobbies = forms_page.check_checkbox()
        filename = forms_page.check_upload()
        state_city = forms_page.check_dropdown()
        forms_page.check_submit_butt()
        os.remove(filename)
        input_info = [f"{firstname} {lastname}", email, gender, str(mobile), f"{day} {month},{year}",
                      subjects, hobbies, filename.split("\\")[-1], address, state_city]
        output_info = forms_page.get_all_fields()
        assert input_info == output_info, "Invalid info"

