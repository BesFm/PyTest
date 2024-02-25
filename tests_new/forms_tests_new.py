import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from conftest import driver
from pages_new.forms_page_new import FormsPage


@allure.suite("Test Form")
class TestForms:
    @allure.title("Test all form")
    def test_all_form(self, driver: WebDriver):
        forms_page = FormsPage(driver=driver)
        forms_page.open()
        assert forms_page.send_input_info() == forms_page.get_output_info(), "Invalid info"
