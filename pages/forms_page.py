import os
from selenium.webdriver import Keys
from generator.generator import generated_person, generated_file, generated_subject, generated_state
from locators.forms_page_locators import FormsPageLocators
from pages.base_page import BasePage
import random


class FormsPage(BasePage):
    locators = FormsPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        firstname = person_info.firstname
        lastname = person_info.lastname
        email = person_info.email
        mobile_number = person_info.mobile_number
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                  "November", "December"]
        birth_input = self.locators.SP
        address = person_info.current_Address
        file_name, path = generated_file()
        subjects = generated_subject()
        state, city = generated_state()
        choose_state = self.element_is_present(self.locators.SELECT_STATE)
        self.remove_element()
        self.element_is_visible(self.locators.INPUT_FIRSTNAME).send_keys(firstname)
        self.element_is_visible(self.locators.INPUT_LASTNAME).send_keys(lastname)
        self.element_is_visible(self.locators.INPUT_EMAIL).send_keys(email)
        self.element_is_visible(self.locators.GENDER_RADIO[random.randint(0, 2)]).click()
        self.element_is_visible(self.locators.MOBILE_NUMBER).send_keys(mobile_number)
        self.element_is_visible(self.locators.DATE_OF_BIRTH).click()
        self.element_is_visible(self.locators.SELECT_MONTH).click()
        self.element_is_present(self.locators.MONTH_OF_BIRTH).click()
        self.element_is_visible(self.locators.SELECT_YEAR).click()
        self.element_is_present(self.locators.YEAR_OF_BIRTH).click()
        self.element_is_visible(self.locators.SELECT_DAY).click()
        for i in subjects:
            self.element_is_visible(self.locators.INPUT_SUBJECTS).send_keys(i)
            self.element_is_visible(self.locators.INPUT_SUBJECTS).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.HOBBIES_CHECKBOX[0]).click()
        self.element_is_visible(self.locators.HOBBIES_CHECKBOX[1]).click()
        self.element_is_visible(self.locators.HOBBIES_CHECKBOX[2]).click()
        self.element_is_visible(self.locators.UPLOAD_PICTURE).send_keys(path)
        self.element_is_visible(self.locators.INPUT_ADDRESS).send_keys(address)
        self.go_to_element(choose_state)
        self.element_is_visible(self.locators.INPUT_STATE).send_keys(state)
        self.element_is_visible(self.locators.INPUT_STATE).send_keys(Keys.RETURN)
        self.element_is_present(self.locators.INPUT_CITY).send_keys(city)
        self.element_is_visible(self.locators.INPUT_CITY).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        os.remove(path)
        student_info = [f"{firstname} {lastname}", email, str(mobile_number),
                        f"{birth_input[2]} {months[int(birth_input[1])]},{birth_input[0]}",
                        ", ".join(subjects),
                        'Sports, Reading, Music', path.split("\\")[-1], address, f"{state} {city}"]
        return student_info

    def get_all_fields(self):
        student_info = self.elements_are_visible(self.locators.OUTPUT_INFO)
        data = []
        for i in student_info:
            data.append(i.text)
        self.element_is_visible(self.locators.CLOSE_TABLE).click()
        del data[2]
        return data
