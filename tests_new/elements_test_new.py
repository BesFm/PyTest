from selenium.webdriver.chrome.webdriver import WebDriver

from Data.data import Answers
from conftest import driver
from pages_new.elements_page_new import TextBoxPageNew, CheckBoxPageNew, RadioButtonPage, WebTablePage, ButtonsPage, \
    LinksPage, UpDownloadPage, DynamicPropertiesPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver: WebDriver):
            text_box_page = TextBoxPageNew(driver=driver)
            text_box_page.open()
            input_name, input_email, input_cur_address, input_perm_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_address, output_perm_address = text_box_page.get_output_info()
            assert input_name == output_name, "Output name difference from expected"
            assert input_email == output_email, "Output email difference from expected"
            assert input_cur_address == output_cur_address, "Output current address difference from expected"
            assert input_perm_address == output_perm_address, "Output permanent address difference from expected"

    class TestCheckBox:

        def test_check_box(self, driver: WebDriver):
            check_box_page = CheckBoxPageNew(driver=driver)
            check_box_page.open()
            assert check_box_page.input_checkbox() == check_box_page.get_output_checkbox(), "Some checkbox not selected"

    class TestRadioButton:

        def test_radio_button(self, driver: WebDriver):
            radio_button_page = RadioButtonPage(driver=driver)
            radio_button_page.open()
            yes_radio, impressive_radio, no_radio = radio_button_page.select_radio_and_get_selected_text()
            assert yes_radio == Answers.YES.value, "RadioButton 'Yes' not valid"
            assert impressive_radio == "Impressive", "RadioButton 'Impressive' not valid"
            assert no_radio == "No", "RadioButton 'No' not valid"

    class TestWebTable:

        def test_web_table_add_person(self, driver: WebDriver):
            web_table_page = WebTablePage(driver=driver)
            web_table_page.open()
            assert web_table_page.add_new_person_return_input_info() in web_table_page.get_all_persons_info(), \
                "New person isn't founded or hasn't been added"

        def test_web_table_search_person(self, driver: WebDriver):
            web_table_page = WebTablePage(driver=driver)
            web_table_page.open()
            assert web_table_page.check_searching_function(), "Person isn't found in the table or hasn't been added"

        def test_web_table_update_person_info(self, driver: WebDriver):
            web_table_page = WebTablePage(driver=driver)
            web_table_page.open()
            assert web_table_page.check_updating_function(), "The Person card hasn't been updated or hasn't been added"

        def test_web_table_delete_person_info(self, driver: WebDriver):
            web_table_page = WebTablePage(driver=driver)
            web_table_page.open()
            assert web_table_page.check_deleting_function(), "The Person card hasn't been deleted or hasn't been added"

        def test_web_table_change_count_row(self, driver: WebDriver):
            web_table_page = WebTablePage(driver=driver)
            web_table_page.open()
            assert web_table_page.select_up_to_some_rows() == [5, 10, 20, 25, 50,
                                                               100], "All of the count rows can't be chosen"

    class TestButtonsClick:

        def test_buttons_click(self, driver: WebDriver):
            button_page = ButtonsPage(driver=driver)
            button_page.open()
            assert button_page.click_on_buttons_and_get_result() == ('You have done a double click',
                                                                     'You have done a right click',
                                                                     'You have done a dynamic click')

    class TestLinks:

        def test_valid_link(self, driver: WebDriver):
            links_page = LinksPage(driver=driver)
            links_page.open()
            assert links_page.click_simple_link_and_get_statuscode(), \
                f"{links_page.click_simple_link_and_get_statuscode()}"

        def test_invalid_links(self, driver: WebDriver):
            links_page = LinksPage(driver=driver)
            links_page.open()
            assert all(links_page.click_another_links_and_check_statuses()), \
                "Some link statuscode difference from expected"

    class TestUploadDownload:
        def test_upload(self, driver: WebDriver):
            up_download_page = UpDownloadPage(driver=driver)
            up_download_page.open()
            assert up_download_page.upload_file(), "Created file hasn't been uploaded"

        def test_download(self, driver: WebDriver):
            up_download_page = UpDownloadPage(driver=driver)
            up_download_page.open()
            assert up_download_page.download_file(), "File hasn't been downloaded"


    class TestDynamicProperties:

        def test_buttons_dynamic_properties(self, driver: WebDriver):
            dynamic_properties_page = DynamicPropertiesPage(driver=driver)
            dynamic_properties_page.open()
            time_enable_change, time_visible_change, time_color_change = dynamic_properties_page.check_page_buttons()
            assert time_enable_change, "Time enable button's property hasn't been changed"
            assert time_visible_change, "Time visible button's property hasn't been changed"
            assert time_color_change, "Time color button's property hasn't been changed"
