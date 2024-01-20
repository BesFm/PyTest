import random
import time

import locators.elements_page_locators
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonPage, LinkPage, \
    UpDownLoadPage
from conftest import driver


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_curr_addr, output_perm_addr = text_box_page.check_filled_form()
            assert full_name == output_name, "ошибка имени"
            assert email == output_email, "ошибка email"
            assert current_address == output_curr_addr, "ошибка текущего адреса"
            assert permanent_address == output_perm_addr, "ошибка постоянного адреса"

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkbox()
            output_checkbox = check_box_page.get_output_checkbox()
            print()
            print(input_checkbox)
            print(output_checkbox)
            assert input_checkbox == output_checkbox, "checkbox is not selected"
            time.sleep(3)

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            radio_button_page.choose_radio_button('yes')
            output_yes = radio_button_page.get_output_radiobutton()
            radio_button_page.choose_radio_button('impressive')
            output_impressive = radio_button_page.get_output_radiobutton()
            radio_button_page.choose_radio_button('no')
            output_no = radio_button_page.get_output_radiobutton()
            assert output_yes == "Yes", "RadioButton 'Yes' not valid"
            assert output_impressive == "Impressive", "RadioButton 'Impressive' not valid"
            assert output_no == "No", "RadioButton 'No' not valid"

    class TestWebTable:

        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_person()
            print(new_person)
            print(table_result)
            assert list(new_person) in table_result

            time.sleep(3)

        def test_wev_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_person(key_word)
            table_result = web_table_page.check_serched_person()
            assert key_word in table_result, "Person wasn't found in the table"

        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_person(lastname)
            age = web_table_page.update_person_info()
            row = web_table_page.check_serched_person()
            print(str(age))
            print(row)
            assert age in row, "The Person card hasn't been changed"

        def test_web_table_delete_person_info(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_person(email)
            web_table_page.delete_person()
            result = web_table_page.check_deleted()
            assert result == "No rows found", "The Person card hasn't been deleted"

        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50, 100], "The count rows can't be chosen"

    class TestButtonClick:

        def test_button_page_different_click(self, driver):
            button_page = ButtonPage(driver, "https://demoqa.com/buttons")
            button_page.open()
            click_result = button_page.click_on_different_button()
            assert click_result == ('You have done a double click',
                                    'You have done a right click',
                                    'You have done a dynamic click')

    class TestLinksPage:

        def test_check_link(self, driver):
            link_page = LinkPage(driver, "https://demoqa.com/links")
            link_page.open()
            href_link, current_url = link_page.check_new_tab_simple_link()
            assert href_link == current_url, "Current link has got another URL than expected"

        def test_broken_links(self, driver):
            link_page = LinkPage(driver, "https://demoqa.com/links")
            link_page.open()
            print()
            link_page.check_another_links()

    class TestUploadAndDownload:

        def test_upload(self, driver):
            upload_download_page = UpDownLoadPage(driver, "https://demoqa.com/upload-download")
            upload_download_page.open()
            file_name, uploaded_file_path = upload_download_page.upload_file()
            assert file_name == uploaded_file_path, "Chosen file isn't uploaded"

        def test_download(self, driver):
            upload_download_page = UpDownLoadPage(driver, "https://demoqa.com/upload-download")
            upload_download_page.open()
            result = upload_download_page.download_file()
            assert result is True, "File isn't downloaded"

