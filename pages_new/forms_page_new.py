import os
import random

import allure
from selenium.webdriver import Keys
from elements.buttons import Button
from elements.input_fields import InputField
from elements.title import Title
from generator.generator import (generated_person, generated_subject, generated_date,
                                 generated_file, generated_state)
from locators.forms_page_locators import FormsPageLocators
from pages.base_page import BasePage


class FormsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, url="https://demoqa.com/automation-practice-form")

        self.firstname_input = InputField(driver=driver,
                                          locator=FormsPageLocators.INPUT_FIRSTNAME)
        self.lastname_input = InputField(driver=driver,
                                         locator=FormsPageLocators.INPUT_LASTNAME)
        self.email_input = InputField(driver=driver,
                                      locator=FormsPageLocators.INPUT_EMAIL)
        self.mobile_input = InputField(driver=driver,
                                       locator=FormsPageLocators.MOBILE_NUMBER)
        self.subjects_input = InputField(driver=driver,
                                         locator=FormsPageLocators.INPUT_SUBJECTS)
        self.address_input = InputField(driver=driver,
                                        locator=FormsPageLocators.INPUT_ADDRESS)
        self.gender_radio_male = InputField(driver=driver,
                                            locator=FormsPageLocators.GENDER_RADIO[0])
        self.gender_radio_female = InputField(driver=driver,
                                              locator=FormsPageLocators.GENDER_RADIO[1])
        self.gender_radio_other = InputField(driver=driver,
                                             locator=FormsPageLocators.GENDER_RADIO[2])
        self.birth_date = Button(driver=driver,
                                 locator=FormsPageLocators.DATE_OF_BIRTH)
        self.select_month = InputField(driver=driver,
                                       locator=FormsPageLocators.SELECT_MONTH)
        self.select_year = InputField(driver=driver,
                                      locator=FormsPageLocators.SELECT_YEAR)
        self.select_day = InputField(driver=driver,
                                     locator=FormsPageLocators.SELECT_DAY)
        self.hobbies_checkbox_sport = Button(driver=driver,
                                             locator=FormsPageLocators.HOBBIES_CHECKBOX[0])
        self.hobbies_checkbox_reading = Button(driver=driver,
                                               locator=FormsPageLocators.HOBBIES_CHECKBOX[1])
        self.hobbies_checkbox_music = Button(driver=driver,
                                             locator=FormsPageLocators.HOBBIES_CHECKBOX[2])
        self.upload_button = Button(driver=driver,
                                    locator=FormsPageLocators.UPLOAD_PICTURE)
        self.select_state = Button(driver=driver,
                                   locator=FormsPageLocators.SELECT_STATE)
        self.state_input = InputField(driver=driver,
                                      locator=FormsPageLocators.INPUT_STATE)
        self.city_input = InputField(driver=driver,
                                     locator=FormsPageLocators.INPUT_CITY)
        self.submit_button = Button(driver=driver,
                                    locator=FormsPageLocators.SUBMIT_BUTTON)
        self.output_list = Title(driver=driver,
                                 locator=FormsPageLocators.OUTPUT_INFO)
        self.close_output = Button(driver=driver,
                                   locator=FormsPageLocators.CLOSE_TABLE)


    @allure.step("Fill inputs")
    def fill_inputs(self) -> tuple:
        person_info = next(generated_person())
        subjects = generated_subject()
        self.firstname_input.is_visible().send_keys(person_info.firstname)
        self.lastname_input.is_visible().send_keys(person_info.lastname)
        self.email_input.is_visible().send_keys(person_info.email)
        self.mobile_input.is_visible().send_keys(person_info.mobile_number)
        for subject in subjects:
            self.subjects_input.is_visible().send_keys(subject)
            self.subjects_input.is_visible().send_keys(Keys.RETURN)
        self.address_input.is_visible().send_keys(person_info.current_Address)
        return (person_info.firstname, person_info.lastname, person_info.email,
                person_info.mobile_number, ", ".join(subjects),
                person_info.current_Address)

    @allure.step("Set gender")
    def click_random_radio(self) -> str:
        gender_choose = random.choice([self.gender_radio_male, self.gender_radio_female,
                                       self.gender_radio_other])
        gender_choose.is_visible().click()
        return gender_choose.is_visible().text

    @allure.step("Set date of birth")
    def set_birth_date(self) -> tuple[str, str, str]:
        date = next(generated_date())
        self.birth_date.is_visible().click()
        self.set_date_by_text(self.select_month.are_visible(), date.month)
        self.set_date_by_text(self.select_year.are_visible(), date.year)
        self.set_date_by_text(self.select_day.are_visible(), str(int(date.day)))
        return date.day, date.month, date.year

    @staticmethod
    def set_date_by_text(element: list, value: str):
        date_list = element
        for item in date_list:
            if item.text == value:
                item.click()
                break

    @allure.step("Set hobbies")
    def click_random_checkboxes(self) -> str:
        first_check, second_check = random.sample((self.hobbies_checkbox_music,
                                                   self.hobbies_checkbox_reading,
                                                   self.hobbies_checkbox_sport), 2)
        first_check.is_visible().click()
        second_check.is_visible().click()
        return f"{first_check.is_visible().text}, {second_check.is_visible().text}"

    @allure.step("Upload file")
    def upload_file(self) -> str:
        path = generated_file()
        self.upload_button.is_visible().send_keys(path)
        return path

    @allure.step("Set state and city")
    def set_state_and_city(self) -> str:
        state, city = generated_state()
        self.go_to_element(self.select_state.is_visible())
        self.state_input.is_visible().send_keys(state)
        self.state_input.is_visible().send_keys(Keys.RETURN)
        self.city_input.is_visible().send_keys(city)
        self.city_input.is_visible().send_keys(Keys.RETURN)
        return f"{state} {city}"

    @allure.step("Click Submit")
    def click_submit_button(self):
        self.submit_button.is_visible().click()

    @allure.step("Get output info")
    def get_output_info(self) -> list[str]:
        student_info = self.output_list.are_visible()
        data = []
        for row in student_info:
            data.append(row.text)
        self.close_output.is_visible().click()
        return data

    @allure.step("Send input info")
    def send_input_info(self) -> list[str]:
        self.remove_element()
        firstname, lastname, email, mobile, subjects, address = self.fill_inputs()
        gender = self.click_random_radio()
        day, month, year = self.set_birth_date()
        hobbies = self.click_random_checkboxes()
        filename = self.upload_file()
        state_city = self.set_state_and_city()
        self.click_submit_button()
        os.remove(filename)
        return [f"{firstname} {lastname}", email, gender, str(mobile),
                f"{day} {month},{year}", subjects, hobbies, filename.split("\\")[-1],
                address, state_city]
