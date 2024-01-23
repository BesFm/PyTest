from pages.forms_page import FormsPage
from conftest import driver


class TestForms:

    def test_all_form(self, driver):
        forms_page = FormsPage(driver, "https://demoqa.com/automation-practice-form")
        forms_page.open()
        input_info = forms_page.fill_all_fields()
        output_info = forms_page.get_all_fields()
        assert input_info == output_info, "Invalid info"

