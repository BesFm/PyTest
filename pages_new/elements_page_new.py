import os
import random
import time

import allure
import requests
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from elements.buttons import Button
from elements.input_fields import InputField
from elements.title import Title
from generator.generator import generated_person, generated_file
from locators.elements_page_locators import (TextBoxPageLocators as TextBoxLocators,
                                             CheckBoxPageLocators as CheckBoxLocators,
                                             RadioButtonPageLocators as RadioLocators,
                                             WebTablePageLocators as WebTableLocators,
                                             ButtonsPageLocators as ButtonsLocators,
                                             LinksPageLocators as LinksLocators,
                                             UpDownLoadPageLocators as DownloadLocators,
                                             DynamicPropertiesPageLocators as DynamicLocators)
from pages.base_page import BasePage


class TextBoxPageNew(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver, url="https://demoqa.com/text-box")
        # инициализация элементов на странице
        self.full_name_field = InputField(driver=driver,
                                          locator=TextBoxLocators.FULL_NAME)
        self.email_field = InputField(driver=driver, locator=TextBoxLocators.EMAIL)
        self.current_address_field = InputField(driver=driver,
                                                locator=TextBoxLocators.CURRENT_ADDRESS)
        self.permanent_address_field = InputField(driver=driver,
                                                  locator=TextBoxLocators.PERMANENT_ADDRESS)
        self.submit_button = Button(driver=driver, locator=TextBoxLocators.SUBMIT)
        self.created_full_name = Button(driver=driver,
                                        locator=TextBoxLocators.CREATED_FULL_NAME)
        self.created_email = Button(driver=driver,
                                    locator=TextBoxLocators.CREATED_EMAIL)
        self.created_current_address = Button(driver=driver,
                                              locator=TextBoxLocators.CREATED_CURRENT_ADDRESS)
        self.created_permanent_address = Button(driver=driver,
                                                locator=TextBoxLocators.CREATED_PERMANENT_ADDRESS)

    @allure.step("Filling all fields")
    def fill_all_fields(self) -> tuple[str, str, str, str]:
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_Address
        permanent_address = person_info.permanent_Address
        self.full_name_field.is_visible().send_keys(full_name)
        self.email_field.is_visible().send_keys(email)
        self.current_address_field.is_visible().send_keys(current_address)
        self.permanent_address_field.is_visible().send_keys(permanent_address)
        self.submit_button.is_visible().click()
        return full_name, email, current_address, permanent_address

    @allure.step("Get output info")
    def get_output_info(self) -> tuple[str, str, str, str]:
        output_full_name = self.created_full_name.is_visible().text.split(":")[-1]
        output_email = self.created_email.is_visible().text.split(":")[-1]
        output_current_address = \
        self.created_current_address.is_visible().text.split(":")[-1]
        output_permanent_address = \
        self.created_permanent_address.is_visible().text.split(":")[-1]
        return output_full_name, output_email, output_current_address, output_permanent_address


class CheckBoxPageNew(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, url="https://demoqa.com/checkbox")
        # инициализация элементов на странице
        self.expand_all_button = Button(driver=driver,
                                        locator=CheckBoxLocators.EXPAND_ALL)
        self.items = Title(driver=driver, locator=CheckBoxLocators.ITEM_LIST)
        self.checked_items = Title(driver=driver,
                                   locator=CheckBoxLocators.CHECKED_ELEMENT)
        self.element_title = Title(driver=driver,
                                   locator=CheckBoxLocators.TITLE_ELEMENT)
        self.result_list = Title(driver=driver,
                                 locator=CheckBoxLocators.OUTPUT_CHECKED)

    @allure.step("Open full checkbox list")
    def open_full_checkbox_list(self):
        self.expand_all_button.is_visible().click()

    @allure.step("Choosing random checkboxes")
    def click_random_checkboxes(self):
        items_list = self.items.are_visible()
        count = 20
        while count > 0:
            item = random.choice(items_list)
            self.go_to_element(item)
            item.click()
            count -= 1

    @allure.step("Get chosen checkboxes")
    def get_checked_checkboxes_text(self) -> list[str]:
        checked_list = self.checked_items.are_visible()
        data = []
        for checkbox in checked_list:
            title_item = checkbox.find_element("xpath",
                                               CheckBoxLocators.TITLE_ELEMENT)
            data.append(title_item.text.lower().replace(" ", "").replace(".doc", ""))
        return data

    @allure.step("Get output checkboxes")
    def get_output_checkbox(self) -> list[str]:
        result_list = self.result_list.are_visible()
        data = []
        for item in result_list:
            data.append(item.text.lower())
        return data

    @allure.step("Input and Get selected checkboxes")
    def input_checkbox(self) -> list[str]:
        self.open_full_checkbox_list()
        self.click_random_checkboxes()
        return self.get_checked_checkboxes_text()


class RadioButtonPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, url="https://demoqa.com/radio-button")
        # инициализация элементов на странице
        self.radio_button_yes = Button(driver=driver,
                                       locator=RadioLocators.YES_RADIO)
        self.radio_button_impressive = Button(driver=driver,
                                              locator=RadioLocators.IMRESSIVE_RADIO)
        self.radio_button_no = Button(driver=driver,
                                      locator=RadioLocators.NO_RADIO)
        self.chosen_radio_title = Title(driver=driver,
                                        locator=RadioLocators.CHOSEN_RADIO)

    @allure.step("Click radio buttons")
    def click_radio_button(self, choice):
        choices = {"yes": self.radio_button_yes,
                   "impressive": self.radio_button_impressive,
                   "no": self.radio_button_no}
        choices[choice].is_visible().click()

    @allure.step("Get output radiobutton")
    def get_output_radiobutton_text(self) -> str:
        return self.chosen_radio_title.is_visible().text

    @allure.step("Select and Get selected radiobutton")
    def select_radio_and_get_selected_text(self) -> tuple[str, str, str]:
        self.click_radio_button("yes")
        yes_rad_title = self.get_output_radiobutton_text()
        self.click_radio_button("impressive")
        impressive_rad_title = self.get_output_radiobutton_text()
        self.click_radio_button("no")
        no_rad_title = self.get_output_radiobutton_text()
        return yes_rad_title, impressive_rad_title, no_rad_title


class WebTablePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, url="https://demoqa.com/webtables")
        # инициализация элементов на странице
        self.add_button = Button(driver=driver, locator=WebTableLocators.ADD_BUTTON)
        self.firstname_input = InputField(driver=driver,
                                          locator=WebTableLocators.FIRSTNAME_INPUT)
        self.lastname_input = InputField(driver=driver,
                                         locator=WebTableLocators.LASTNAME_INPUT)
        self.email_input = InputField(driver=driver,
                                      locator=WebTableLocators.EMAIL_INPUT)
        self.age_input = InputField(driver=driver,
                                    locator=WebTableLocators.AGE_INPUT)
        self.salary_input = InputField(driver=driver,
                                       locator=WebTableLocators.SALARY_INPUT)
        self.departament_input = InputField(driver=driver,
                                            locator=WebTableLocators.DEPARTAMENT_INPUT)
        self.submit_button = Button(driver=driver,
                                    locator=WebTableLocators.SUBMIT)
        self.person_info = Title(driver=driver,
                                 locator=WebTableLocators.PERSON_INFO)
        self.search_field = InputField(driver=driver,
                                       locator=WebTableLocators.SEARCH_FIELD)
        self.update_button = Button(driver=driver,
                                    locator=WebTableLocators.UPDATE_BUTTON)
        self.delete_button = Button(driver=driver,
                                    locator=WebTableLocators.DELETE_BUTTON)
        self.count_row_list = Title(driver=driver,
                                    locator=WebTableLocators.COUNT_ROW_LIST)
        self.title_after_delete = Title(driver=driver,
                                        locator=WebTableLocators.CHECK_DELETED)

    @allure.step("Add new persons")
    def add_new_person_return_input_info(self, count=2) -> list[str]:
        person_list = []
        while count > 0:
            person_info = next(generated_person())
            firstname = person_info.firstname
            lastname = person_info.lastname
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.add_button.is_visible().click()
            self.firstname_input.is_visible().send_keys(firstname)
            self.lastname_input.is_visible().send_keys(lastname)
            self.email_input.is_visible().send_keys(email)
            self.age_input.is_visible().send_keys(age)
            self.salary_input.is_visible().send_keys(salary)
            self.departament_input.is_visible().send_keys(department)
            self.submit_button.is_visible().click()

            count -= 1
            person_list.append(
                [firstname, lastname, str(age), email, str(salary), department])
        return random.choice(person_list)

    @allure.step("Get person info")
    def get_all_persons_info(self) -> list[str]:
        time.sleep(0.5)
        person_info = self.person_info.are_visible()
        data = []
        for item in person_info:
            data.append(item.text.splitlines())
        return data

    @allure.step("Search person by keyword")
    def search_person(self, key_words):
        self.search_field.is_visible().send_keys(key_words)

    @allure.step("Update person info")
    def update_person_info(self) -> str:
        person_info = next(generated_person())
        age = person_info.age
        self.update_button.is_visible().click()
        self.age_input.is_visible().send_keys(age)
        self.submit_button.is_visible().click()
        return str(age)

    @allure.step("Delete person")
    def delete_person(self):
        self.delete_button.is_visible().click()
        return self.title_after_delete.is_visible().text

    @allure.step("Select certain count of rows")
    def select_up_to_some_rows(self) -> list[int]:
        self.remove_element()
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for x in count:
            self.go_to_element(self.count_row_list.is_visible())
            self.count_row_list.is_visible().click()
            self.element_is_visible((By.CSS_SELECTOR, f"option[value='{x}']")).click()
            data.append(self.get_count_rows())
        return data

    @allure.step("Get count rows")
    def get_count_rows(self) -> int:
        list_rows = self.person_info.are_present()
        return len(list_rows)

    @allure.step("Check searching function")
    def check_searching_function(self):
        added_person_info = self.add_new_person_return_input_info()
        keyword = random.choice(added_person_info)
        self.search_person(key_words=keyword)
        searched_person_info = self.person_info.is_visible().text
        return added_person_info == searched_person_info.splitlines()

    @allure.step("Check updating function")
    def check_updating_function(self):
        added_person_info = self.add_new_person_return_input_info()
        keyword = random.choice(added_person_info)
        self.search_person(key_words=keyword)
        persons_new_age = self.update_person_info()
        self.search_person(persons_new_age)
        updated_person = self.person_info.is_visible()
        return updated_person != added_person_info

    @allure.step("Check deleting function")
    def check_deleting_function(self):
        added_person_info = self.add_new_person_return_input_info()
        keyword = random.choice(added_person_info)
        self.search_person(key_words=keyword)
        result_text = self.delete_person()
        return result_text == "No rows found"


class ButtonsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, url="https://demoqa.com/buttons")

        self.double_click_button = Button(driver=driver,
                                          locator=ButtonsLocators.DOUBLE_CLICK_ME)
        self.right_click_button = Button(driver=driver,
                                         locator=ButtonsLocators.RIGHT_CLICK_ME)
        self.left_click_button = Button(driver=driver,
                                        locator=ButtonsLocators.CLICK_ME)
        self.double_click_result = Title(driver=driver,
                                         locator=ButtonsLocators.DOUBLE_CLICK_RESULT)
        self.right_click_result = Title(driver=driver,
                                        locator=ButtonsLocators.RIGHT_CLICK_RESULT)
        self.left_click_result = Title(driver=driver,
                                       locator=ButtonsLocators.CLICK_ME_RESULT)

    @allure.step("Make different click on buttons")
    def click_on_buttons_and_get_result(self) -> tuple[str, str, str]:
        self.action_double_click(self.double_click_button.is_visible())
        self.action_right_click(self.right_click_button.is_visible())
        self.left_click_button.is_visible().click()
        return self.get_click_result(self.double_click_result), self.get_click_result(
            self.right_click_result), self.get_click_result(self.left_click_result)

    @staticmethod
    @allure.step("Get click result")
    def get_click_result(element) -> str:
        return element.is_visible().text


class LinksPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, url="https://demoqa.com/links")

        self.simple_link = Button(driver=driver,
                                  locator=LinksLocators.SIMPLE_LINK)
        self.creating_link = Button(driver=driver,
                                    locator=LinksLocators.CREATED_LINK)
        self.no_content_link = Button(driver=driver,
                                      locator=LinksLocators.NO_CONTENT_LINK)
        self.moved_link = Button(driver=driver,
                                 locator=LinksLocators.MOVED_LINK)
        self.bed_request_link = Button(driver=driver,
                                       locator=LinksLocators.BED_REQUEST_LINK)
        self.unauthorized_link = Button(driver=driver,
                                        locator=LinksLocators.UNAUTHORIZED_LINK)
        self.forbidden_link = Button(driver=driver,
                                     locator=LinksLocators.FORBIDDEN_LINK)
        self.not_found_link = Button(driver=driver,
                                     locator=LinksLocators.NOT_FOUND_LINK)
        self.links_result_title = Title(driver=driver,
                                        locator=LinksLocators.LINKS_RESULT_TITLE)

    @allure.step("Click new tab link")
    def click_simple_link_and_get_statuscode(self) -> bool | str:
        simple_link_href = self.simple_link.is_visible().get_attribute("href")
        request = requests.get(simple_link_href)
        if request.status_code == 200:
            self.simple_link.is_visible().click()
            self.driver.switch_to.window(self.driver.window_handles[-1])
            url = self.driver.current_url
            return simple_link_href == url
        else:
            return f"{simple_link_href} link give status code {request.status_code}"

    @allure.step("Click non-working links")
    def click_another_links_and_check_statuses(self) -> list[bool]:
        status_list = []
        simple_link_href = self.simple_link.is_visible().get_attribute("href")
        links_dictic = {"created": self.creating_link, "no-content": self.no_content_link,
                        "moved": self.moved_link, "bad-request": self.bed_request_link,
                        "unauthorized": self.unauthorized_link,
                        "forbidden": self.forbidden_link,
                        "invalid-url": self.not_found_link}
        for handle, webelement in links_dictic.items():
            request = requests.get(f"{simple_link_href}{handle}")
            self.go_to_element(webelement.is_visible())
            webelement.is_visible().click()
            time.sleep(0.5)
            status_list.append(
                str(request.status_code) in self.links_result_title.is_visible().text
            )
        return status_list


class UpDownloadPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, url="https://demoqa.com/upload-download")

        self.upload_button = Button(driver=driver,
                                    locator=DownloadLocators.UPLOAD_BUTTON)
        self.upload_file_path = Button(driver=driver,
                                       locator=DownloadLocators.UPLOAD_FILE_PATH)
        self.download_button = Button(driver=driver,
                                      locator=DownloadLocators.DOWNLOAD_BUTTON)

    @allure.step("Upload file")
    def upload_file(self) -> bool:
        path = generated_file()
        self.upload_button.is_visible().send_keys(path)
        uploaded_file_path = self.upload_file_path.is_visible().text
        os.remove(path)
        return path.split("\\")[-1] == uploaded_file_path.split("\\")[-1]

    @allure.step("Download file")
    def download_file(self) -> bool:
        self.download_button.is_visible().click()
        time.sleep(2)
        expected_path = rf"C:\Users\Bes.fm\Downloads\sampleFile.jpeg"
        check_file = os.path.exists(expected_path)
        os.remove(expected_path)
        return check_file


class DynamicPropertiesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, url="https://demoqa.com/dynamic-properties")

        self.color_change_button = Button(driver=driver,
                                          locator=DynamicLocators.COLOR_CHANGE_BUTTON)
        self.time_enable_button = Button(driver=driver,
                                         locator=DynamicLocators.ENABLE_IN_BUTTON)
        self.time_visible_button = Button(driver=driver,
                                          locator=DynamicLocators.VISIBLE_IN_BUTTON)

    @allure.step("Click page buttons")
    def check_page_buttons(self) -> tuple[bool | None, bool | None, bool]:
        time_enable_result, time_visible_result = None, None
        first_button_color = self.color_change_button.is_visible().value_of_css_property(
            "color")
        try:
            self.time_enable_button.is_clickable(set_timeout=0.5)
        except TimeoutException:
            time_enable_result = True
        try:
            self.time_visible_button.is_visible(set_timeout=0.5)
        except TimeoutException:
            time_visible_result = True

        time.sleep(5)

        changed_button_color = self.color_change_button.is_visible().value_of_css_property(
            "color")
        try:
            self.time_enable_button.is_clickable()
        except TimeoutException:
            time_enable_result = False
        try:
            self.time_visible_button.is_visible()
        except TimeoutException:
            time_visible_result = False
        return time_enable_result, time_visible_result, (
                    first_button_color != changed_button_color)
