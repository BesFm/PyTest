import random

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators
from generator.generator import generated_colors, generated_date


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def get_wili_accord_text(self):
        try:
            return self.element_is_visible(self.locators.WHATISLOREMIPSUM_TEXT).text
        except TimeoutException:
            self.element_is_visible(self.locators.WHATISLOREMIPSUM_ACCORD).click()
            return self.element_is_visible(self.locators.WHATISLOREMIPSUM_TEXT).text

    def get_wdicf_accord_text(self):
        try:
            return self.element_is_visible(self.locators.WHATDOESITCOMEFROM_TEXT).text
        except TimeoutException:
            self.element_is_visible(self.locators.WHATDOESITCOMEFROM_ACCORD).click()
            return self.element_is_visible(self.locators.WHATDOESITCOMEFROM_TEXT).text

    def get_wdwui_accord_text(self):
        try:
            return self.element_is_visible(self.locators.WHYDOWEUSEIT_TEXT).text
        except TimeoutException:
            self.element_is_visible(self.locators.WHYDOWEUSEIT_ACCORD).click()
            return self.element_is_visible(self.locators.WHYDOWEUSEIT_TEXT).text


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    def fill_multiple_color_input(self):
        color = random.sample(generated_colors(), 3)
        result = []
        mult_input_button = self.element_is_visible(self.locators.MULTIPLE_COLOR_INPUT)
        for i in range(3):
            mult_input_button.send_keys(color[i])
            mult_input_button.send_keys(Keys.ENTER)
            result.append(self.elements_are_visible(self.locators.MULTI_INPUT_RESULT)[i].text)
        return color, result

    def remove_each_colors_from_input(self):
        for i in range(3):
            self.element_is_visible(self.locators.DELETE_ONE_COLOR).click()
        try:
            return self.element_is_visible(self.locators.MULTI_INPUT_RESULT).text
        except TimeoutException:
            return None

    def remove_all_colors_from_input(self):
        self.element_is_visible(self.locators.DELETE_ALL_COLORS).click()
        try:
            return self.element_is_visible(self.locators.MULTI_INPUT_RESULT).text
        except TimeoutException:
            return None

    def fill_single_color_input(self):
        color = random.choice(generated_colors())
        self.element_is_visible(self.locators.SINGLE_COLOR_INPUT).send_keys(color)
        self.element_is_visible(self.locators.SINGLE_COLOR_INPUT).send_keys(Keys.ENTER)
        return color, self.element_is_visible(self.locators.SINGLE_INPUT_RESULT).text


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    def set_date(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.INPUT_DATE)
        previous_date = input_date.get_attribute("value")
        input_date.click()
        self.set_item_by_text(self.locators.SELECT_MONTH, date.month)
        self.set_item_by_text(self.locators.SELECT_YEAR, date.year)
        self.set_item_from_date_list(self.locators.SELECT_DAY, str(int(date.day)))
        result_date = input_date.get_attribute("value")
        return previous_date, result_date

    def set_time_date(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.TIME_DATE_INPUT)
        previous_date = input_date.get_attribute("value")
        input_date.click()
        self.element_is_visible(self.locators.TIME_DATE_MONTH_DROP).click()
        self.set_item_from_date_list(self.locators.TIME_DATE_SELECT_MONTH, date.month)
        self.element_is_visible(self.locators.TIME_DATE_YEAR_DROP).click()
        self.set_year_for_time_date_picker(self.locators.TIME_DATE_SELECT_YEAR, date.year)
        self.set_item_from_date_list(self.locators.SELECT_DAY, date.day)
        self.set_item_from_date_list(self.locators.TIME_DATE_SELECT_TIME, date.time)
        result_date = input_date.get_attribute("value")
        return previous_date, result_date

    def set_item_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    def set_item_from_date_list(self, element, value):
        items_list = self.elements_are_visible(element)
        for item in items_list:
            if item.text == value:
                item.click()
                break

    def set_year_for_time_date_picker(self, element, value):
        item_list = self.elements_are_visible(element)
        while True:
            item = item_list[1]
            if item.text == value:
                item.click()
                break
            else:
                self.element_is_visible(self.locators.TIME_DATE_YEAR_SEARCH_OLD).click()
                item_list = self.elements_are_visible(element)
