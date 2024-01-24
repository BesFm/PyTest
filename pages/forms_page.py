import os
from selenium.webdriver import Keys
from generator.generator import generated_person, generated_file, generated_subject, generated_state
from locators.forms_page_locators import FormsPageLocators
from pages.base_page import BasePage
import random


class FormsPage(BasePage):
    locators = FormsPageLocators()

    def remove_banners(self):
        self.remove_element()

    def check_inputs(self):
        person_info = next(generated_person())
        subjects = generated_subject()
        self.element_is_visible(self.locators.INPUT_FIRSTNAME).send_keys(person_info.firstname)
        self.element_is_visible(self.locators.INPUT_LASTNAME).send_keys(person_info.lastname)
        self.element_is_visible(self.locators.INPUT_EMAIL).send_keys(person_info.email)
        self.element_is_visible(self.locators.MOBILE_NUMBER).send_keys(person_info.mobile_number)
        for i in subjects:
            self.element_is_visible(self.locators.INPUT_SUBJECTS).send_keys(i)
            self.element_is_visible(self.locators.INPUT_SUBJECTS).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.INPUT_ADDRESS).send_keys(person_info.current_Address)
        return (person_info.firstname, person_info.lastname, person_info.email, person_info.mobile_number,
                ", ".join(subjects), person_info.current_Address)

    def check_radio_butt(self):
        r = random.randint(0, 2)
        self.element_is_visible(self.locators.GENDER_RADIO[r]).click()
        return self.element_is_visible(self.locators.GENDER_RADIO[r]).text

    def check_calendar(self):
        self.element_is_visible(self.locators.DATE_OF_BIRTH).click()
        self.element_is_visible(self.locators.SELECT_MONTH).click()
        self.element_is_present(self.locators.MONTH_OF_BIRTH).click()
        self.element_is_visible(self.locators.SELECT_YEAR).click()
        self.element_is_present(self.locators.YEAR_OF_BIRTH).click()
        self.element_is_visible(self.locators.SELECT_DAY).click()
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                  "November", "December"]
        return self.locators.SP[2], months[int(self.locators.SP[1])], self.locators.SP[0]

    def check_checkbox(self):
        self.element_is_visible(self.locators.HOBBIES_CHECKBOX[0]).click()
        self.element_is_visible(self.locators.HOBBIES_CHECKBOX[1]).click()
        self.element_is_visible(self.locators.HOBBIES_CHECKBOX[2]).click()
        return 'Sports, Reading, Music'

    def check_upload(self):
        path = generated_file()
        self.element_is_visible(self.locators.UPLOAD_PICTURE).send_keys(path)
        return path

    def check_dropdown(self):
        state, city = generated_state()
        self.go_to_element(self.element_is_present(self.locators.SELECT_STATE))
        self.element_is_visible(self.locators.INPUT_STATE).send_keys(state)
        self.element_is_visible(self.locators.INPUT_STATE).send_keys(Keys.RETURN)
        self.element_is_present(self.locators.INPUT_CITY).send_keys(city)
        self.element_is_visible(self.locators.INPUT_CITY).send_keys(Keys.RETURN)
        return f"{state} {city}"

    def check_submit_butt(self):
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    def get_all_fields(self):
        student_info = self.elements_are_visible(self.locators.OUTPUT_INFO)
        data = []
        for i in student_info:
            data.append(i.text)
        self.element_is_visible(self.locators.CLOSE_TABLE).click()
        return data
