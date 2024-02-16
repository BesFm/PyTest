import allure
from selenium.webdriver import Keys
from generator.generator import generated_person, generated_file, generated_subject, generated_state, generated_date
from locators.forms_page_locators import FormsPageLocators
from pages.base_page import BasePage
import random


class FormsPage(BasePage):
    locators = FormsPageLocators()

    # убрать баннер рекламы
    def remove_banners(self):
        self.remove_element()

    @allure.step("Fill inputs")
    def fill_inputs(self):
        person_info = next(generated_person())
        subjects = generated_subject()
        with allure.step("Filling inputs"):
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

    @allure.step("Set gender")
    def click_radio_butt(self):
        r = random.randint(0, 2)
        self.element_is_visible(self.locators.GENDER_RADIO[r]).click()
        return self.element_is_visible(self.locators.GENDER_RADIO[r]).text
    
    @allure.step("Set date of birth")
    def set_birth_data(self):
        date = next(generated_date())
        self.element_is_visible(self.locators.DATE_OF_BIRTH).click()
        self.set_date_by_text(self.locators.SELECT_MONTH, date.month)
        self.set_date_by_text(self.locators.SELECT_YEAR, date.year)
        self.set_date_by_text(self.locators.SELECT_DAY, str(int(date.day)))
        return date.day, date.month, date.year
    
    def set_date_by_text(self, element, value):  # установки даты
        date_list = self.elements_are_visible(element)
        for item in date_list:
            if item.text == value:
                item.click()
                break
    
    @allure.step("Set all hobbies")
    def click_all_checkboxes(self):
        self.element_is_visible(self.locators.HOBBIES_CHECKBOX[0]).click()
        self.element_is_visible(self.locators.HOBBIES_CHECKBOX[1]).click()
        self.element_is_visible(self.locators.HOBBIES_CHECKBOX[2]).click()
        return (f"{self.element_is_visible(self.locators.HOBBIES_CHECKBOX[0]).text},"
                f" {self.element_is_visible(self.locators.HOBBIES_CHECKBOX[1]).text},"
                f" {self.element_is_visible(self.locators.HOBBIES_CHECKBOX[2]).text}")

    @allure.step("Upload file")
    def upload_file(self):
        path = generated_file()
        self.element_is_visible(self.locators.UPLOAD_PICTURE).send_keys(path)
        return path

    @allure.step("Set state and city")
    def set_state_city(self):
        state, city = generated_state()
        self.go_to_element(self.element_is_present(self.locators.SELECT_STATE))
        self.element_is_visible(self.locators.INPUT_STATE).send_keys(state)
        self.element_is_visible(self.locators.INPUT_STATE).send_keys(Keys.RETURN)
        self.element_is_present(self.locators.INPUT_CITY).send_keys(city)
        self.element_is_visible(self.locators.INPUT_CITY).send_keys(Keys.RETURN)
        return f"{state} {city}"

    @allure.step("Send filled form")
    def click_submit_butt(self):
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

    @allure.step("Get output form")
    def get_output_info(self):
        student_info = self.elements_are_visible(self.locators.OUTPUT_INFO)
        data = []
        for i in student_info:
            data.append(i.text)
        self.element_is_visible(self.locators.CLOSE_TABLE).click()
        return data
