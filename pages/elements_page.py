import base64
import os
import random
import time

import allure
import requests
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators, ButtonsPageLocators, LinksPageLocators, UpDownLoadPageLocators, DynamicPropertiesPageLocators
from pages.base_page import BasePage
from generator.generator import generated_person, generated_file


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    @allure.step("Filling all fields")
    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_Address
        permanent_address = person_info.permanent_Address
        with allure.step("Filling fields"):
            self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
            self.element_is_visible(self.locators.EMAIL).send_keys(email)
            self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
            self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        with allure.step("Click Submit"):
            self.element_is_clickable(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    @allure.step("Get output info")
    def get_output_info(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(":")[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(":")[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(":")[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(":")[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    @allure.step("Open full checkbox list")
    def open_full_checkbox_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL).click()

    @allure.step("Choosing random checkboxes")
    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 20
        while count > 0:
            item = item_list[random.randint(1, 15)]
            self.go_to_element(item)
            item.click()
            count -= 1

    @allure.step("Get chosen checkboxes")
    def get_checked_checkbox(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ELEMENT)
        data = []
        for box in checked_list:
            title_item = box.find_element("xpath", self.locators.TITLE_ELEMENT)
            data.append(title_item.text.lower().replace(" ", "").replace(".doc", ""))
        return data

    @allure.step("Get output checkboxes")
    def get_output_checkbox(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_CHECKED)
        data = []
        for item in result_list:
            data.append(item.text.lower())
        return data


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    @allure.step("Click radio buttons")
    def click_radio_button(self, choice):
        choices = {"yes": self.locators.YES_RADIO,
                   "impressive": self.locators.IMRESSIVE_RADIO,
                   "no": self.locators.NO_RADIO}
        with allure.step(f"Click {choice} radiobutton"):
            self.element_is_visible(choices[choice]).click()

    @allure.step("Get output radiobutton")
    def get_output_radiobutton(self):
        return self.element_is_present(self.locators.CHOSEN_RADIO).text


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    @allure.step("Add new persons")
    def add_new_person(self, count=2):
        person_list = []
        while count > 0:
            person_info = next(generated_person())
            firstname = person_info.firstname
            lastname = person_info.lastname
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            with allure.step("Filling person form"):
                self.element_is_visible(self.locators.ADD_BUTTON).click()
                self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(firstname)
                self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(lastname)
                self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
                self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
                self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
                self.element_is_visible(self.locators.DEPARTAMENT_INPUT).send_keys(department)
            with allure.step("Click Submit button"):
                self.element_is_visible(self.locators.SUBMIT).click()
            count -= 1
            person_list.append([firstname, lastname, str(age), email, str(salary), department])
        return person_list

    @allure.step("Get person info")
    def get_new_person_info(self):
        time.sleep(0.5)
        person_info = self.elements_are_present(self.locators.PERSON_INFO)
        data = []
        for item in person_info:
            data.append(item.text.splitlines())
        return data

    @allure.step("Search person by keyword")
    def search_person(self, key_words):
        self.element_is_visible(self.locators.SEARCH_FIELD).send_keys(key_words)

    @allure.step("Get searched person info")
    def get_searched_person_info(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element("xpath", self.locators.ROW_PARENT)
        return row.text.splitlines()

    @allure.step("Update person info")
    def update_person_info(self):
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visible(self.locators.UPDATE_BUTTON).click()
        self.element_is_visible(self.locators.AGE_INPUT).clear()
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT).click()
        return str(age)

    @allure.step("Delete person")
    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()
        return self.element_is_present(self.locators.CHECK_DELETED).text

    @allure.step("Select certain count of rows")
    def select_up_to_some_rows(self):
        self.remove_element()
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for x in count:
            count_row_button = self.element_is_visible(self.locators.COUNT_ROW_LIST)
            self.go_to_element(count_row_button)
            count_row_button.click()
            self.element_is_visible((By.CSS_SELECTOR, f"option[value='{x}']")).click()
            data.append(self.get_count_rows())
        return data

    @allure.step("Get count rows")
    def get_count_rows(self):
        list_rows = self.elements_are_present(self.locators.PERSON_INFO)
        return len(list_rows)


class ButtonPage(BasePage):
    locators = ButtonsPageLocators()

    @allure.step("Make different click on buttons")
    def click_on_different_button(self):
        self.action_double_click(self.element_is_visible(self.locators.DOUBLE_CLICK_ME))
        self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_ME))
        self.element_is_visible(self.locators.CLICK_ME).click()
        return (self.get_click_result(self.locators.DOUBLE_CLICK_RESULT),
                self.get_click_result(self.locators.RIGHT_CLICK_RESULT),
                self.get_click_result(self.locators.CLICK_ME_RESULT))

    @allure.step("Get click result")
    def get_click_result(self, element):
        return self.element_is_present(element).text


class LinkPage(BasePage):
    locators = LinksPageLocators()

    @allure.step("Click new tab link")
    def click_new_tab_simple_link(self):
        simple_link = self.element_is_visible(self.locators.SIMPLE_LINK)
        link_href = simple_link.get_attribute("href")
        request = requests.get(link_href)
        if request.status_code == 200:
            simple_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return link_href, url
        else:
            return f'Status code is {request.status_code}', link_href

    @allure.step("Click non-working links")
    def click_another_links(self):
        simple_link = self.element_is_visible(self.locators.SIMPLE_LINK)
        link_href = simple_link.get_attribute("href")  # берет атрибут "href" элемента из дом-дерева
        links_list = ["created", "no-content", "moved", "bad-request", "unauthorized", "forbidden", "invalid-url"]
        links_locators_list = [self.locators.CREATED_LINK, self.locators.NO_CONTENT_LINK, self.locators.MOVED_LINK,
                               self.locators.BED_REQUEST_LINK, self.locators.UNAUTHORIZED_LINK,
                               self.locators.FORBIDDEN_LINK, self.locators.NOT_FOUND_LINK]
        for i in range(len(links_list)):
            request = requests.get(f"{link_href}{links_list[i]}")
            if request.status_code == 200:
                simple_link.click()
                self.element_is_present(links_locators_list[i]).click()
            else:
                print(f'Status code is {request.status_code}, {self.element_is_present(links_locators_list[i]).text}')


class UpDownLoadPage(BasePage):
    locators = UpDownLoadPageLocators()

    @allure.step("Upload file")
    def upload_file(self):
        path = generated_file()
        self.element_is_visible(self.locators.UPLOAD_BUTTON).send_keys(path)
        uploaded_file_path = self.element_is_present(self.locators.UPLOAD_FILE_PATH).text
        time.sleep(3)
        os.remove(path)
        return path.split("\\")[-1], uploaded_file_path.split("\\")[-1]

    @allure.step("Download file")
    def download_file(self):
        link = self.element_is_visible(self.locators.DOWNLOAD_BUTTON).get_attribute("href")
        link_b = base64.b64decode(link.split(",")[1])
        path_name_file = rf"C:\Users\Bes.fm\Downloads\filetest{random.randint(0, 500)}.jpeg"
        with open(path_name_file, "wb+") as f:
            f.write(link_b)
            check_file = os.path.exists(path_name_file)
            f.close()
        time.sleep(3)
        os.remove(path_name_file)
        return check_file


class DynamicPropertiesPage(BasePage):
    locators = DynamicPropertiesPageLocators()

    @allure.step("Click page buttons")
    def click_page_buttons(self):
        with allure.step("Color Button"):
            color_button = self.element_is_present(self.locators.COLOR_CHANGE_BUTTON)
            color_button_before = color_button.value_of_css_property("color")
            time.sleep(5)
            color_button_after = color_button.value_of_css_property("color")
            color_changed = color_button_before != color_button_after
        with allure.step("Not Available Button"):
            not_av_button_enable = True
            try:
                self.element_is_clickable(self.locators.ENABLE_IN_BUTTON)
            except TimeoutException:
                not_av_button_enable = False
        with allure.step("Not Visible Button"):
            not_vis_button_enable = True
            try:
                self.element_is_visible(self.locators.VISIBLE_IN_BUTTON)
            except TimeoutException:
                not_vis_button_enable = False

        return not_av_button_enable, color_changed, not_vis_button_enable

    def get_enable_button(self):
        try:
            self.element_is_clickable(self.locators.ENABLE_IN_BUTTON)
        except TimeoutException:
            return False
        return True

    def button_changed_color(self):
        color_button = self.element_is_present(self.locators.COLOR_CHANGE_BUTTON)
        color_button_before = color_button.value_of_css_property("color")
        time.sleep(5)
        color_button_after = color_button.value_of_css_property("color")
        return color_button_after, color_button_before

    def get_appear_button(self):
        try:
            self.element_is_visible(self.locators.VISIBLE_IN_BUTTON)
        except TimeoutException:
            return False
        return True
