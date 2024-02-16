import random

import allure

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonPage, LinkPage, \
    UpDownLoadPage, DynamicPropertiesPage
from conftest import driver


@allure.suite("Elements")
class TestElements:
    @allure.feature("TextBox")
    class TestTextBox:
        @allure.title("Test TextBox")
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_curr_addr, output_perm_addr = text_box_page.get_output_info()
            assert full_name == output_name, "Output name difference from expected"
            assert email == output_email, "Output email difference from expected"
            assert current_address == output_curr_addr, "Output current address difference from expected"
            assert permanent_address == output_perm_addr, "Output permanent address difference from expected"

    @allure.feature("CheckBox")
    class TestCheckBox:
        @allure.title("Test CheckBox")
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            assert check_box_page.input_checkbox() == check_box_page.get_output_checkbox(), "Some checkbox not selected"

    @allure.feature("RadioButtons")
    class TestRadioButton:
        @allure.title("Test RadioButton")
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            output_yes, output_impressive, output_no = radio_button_page.select_and_get_selected_radiobutton()
            assert output_yes == "Yes", "RadioButton 'Yes' not valid"
            assert output_impressive == "Impressive", "RadioButton 'Impressive' not valid"
            assert output_no == "No", "RadioButton 'No' not valid"

    @allure.feature("Web Table")
    class TestWebTable:
        @allure.title("Web Table: Add Person")
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            assert web_table_page.add_new_person() in web_table_page.get_new_person_info(), \
                "New person isn't founded or hasn't been added"

        @allure.title("Web Table: Search Person")
        def test_wev_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            assert web_table_page.check_searching_function(), "Person isn't found in the table or hasn't been added"

        @allure.title("Web Table: Update Person")
        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            assert web_table_page.check_updating_function(), "The Person card hasn't been updated or hasn't been added"

        @allure.title("Web Table: Delete Person")
        def test_web_table_delete_person_info(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            assert web_table_page, "The Person card hasn't been deleted or hasn't been added"

        @allure.title("Web Table: Change row count")
        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50, 100], "All of the count rows can't be chosen"

    @allure.feature("Button Click")
    class TestButtonClick:
        @allure.title("Test different click")
        def test_button_page_different_click(self, driver):
            button_page = ButtonPage(driver, "https://demoqa.com/buttons")
            button_page.open()
            assert button_page.click_on_different_button() == ('You have done a double click',
                                                               'You have done a right click',
                                                               'You have done a dynamic click')

    @allure.feature("Links")
    class TestLinksPage:
        @allure.title("Test normal links")
        def test_check_link(self, driver):
            link_page = LinkPage(driver, "https://demoqa.com/links")
            link_page.open()
            assert link_page.click_new_tab_simple_link(), "Current link has got another URL than expected"

        @allure.title("Test broken links")
        def test_broken_links(self, driver):
            link_page = LinkPage(driver, "https://demoqa.com/links")
            link_page.open()
            assert 200 not in link_page.click_another_links(), "Some link give status code 200"

    @allure.feature("Upload and Download")
    class TestUploadAndDownload:
        @allure.title("Test upload")
        def test_upload(self, driver):
            upload_download_page = UpDownLoadPage(driver, "https://demoqa.com/upload-download")
            upload_download_page.open()
            assert upload_download_page.upload_file(), "Chosen file isn't uploaded"

        @allure.title("Test download")
        def test_download(self, driver):
            upload_download_page = UpDownLoadPage(driver, "https://demoqa.com/upload-download")
            upload_download_page.open()
            assert upload_download_page.download_file() is True, "File isn't downloaded"

    @allure.feature("Dynamic Properties")
    class TestDynamicProperties:
        # отсчет реального времени начинается после появления начальных кнопок (в каждом тесте этого класса)
        # отсчет timeout начинается после окончания загрузки страницы
        @allure.title("Test all buttons")
        def test_all_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
            dynamic_properties_page.open()
            button_enabled, color_changed, button_visible = dynamic_properties_page.click_page_buttons()
            assert button_enabled is True, "'Enable after 5sec' Button isn't available after timeout"
            assert color_changed is True, "Button color isn't changed after timeout"
            assert button_visible is True, "Button isn't appear after timeout"

        def test_enable_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
            dynamic_properties_page.open()
            button_is_enable = dynamic_properties_page.get_enable_button()
            assert button_is_enable is True, "'Enable after 5sec' Button isn't available after timeout"

        def test_color_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
            dynamic_properties_page.open()
            color_after, color_before = dynamic_properties_page.button_changed_color()
            assert color_after != color_before, "Button color isn't changed after timeout"

        def test_appear_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
            dynamic_properties_page.open()
            button_is_appear = dynamic_properties_page.get_appear_button()
            assert button_is_appear is True, "Button isn't appear after timeout"
