import random
import time

import allure
from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from locators.widgets_page_locators import (AccordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators,
                                            SliderPageLocators, ProgressBarPageLocators, TabsPageLocators,
                                            ToolTipsPageLocators, MenuPageLocators, SelectMenuPageLocators)
from generator.generator import generated_colors, generated_date


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    @allure.step("Read 'What is Lorem Ipsum?' accord text")
    def get_wili_accord_text(self) -> str:
        try:
            return self.element_is_visible(self.locators.WHATISLOREMIPSUM_TEXT).text
        except TimeoutException:
            self.element_is_visible(self.locators.WHATISLOREMIPSUM_ACCORD).click()
            return self.element_is_visible(self.locators.WHATISLOREMIPSUM_TEXT).text

    @allure.step("Read 'Where does it come from?' accord text")
    def get_wdicf_accord_text(self) -> str:
        try:
            return self.element_is_visible(self.locators.WHATDOESITCOMEFROM_TEXT).text
        except TimeoutException:
            self.element_is_visible(self.locators.WHATDOESITCOMEFROM_ACCORD).click()
            return self.element_is_visible(self.locators.WHATDOESITCOMEFROM_TEXT).text

    @allure.step("Read 'Why do we use it?' accord text")
    def get_wdwui_accord_text(self) -> str:
        try:
            return self.element_is_visible(self.locators.WHYDOWEUSEIT_TEXT).text
        except TimeoutException:
            self.element_is_visible(self.locators.WHYDOWEUSEIT_ACCORD).click()
            return self.element_is_visible(self.locators.WHYDOWEUSEIT_TEXT).text


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    @allure.step("Fill multiple color input")
    def fill_multiple_color_input(self) -> tuple[list[str], list[str]]:
        color = next(generated_colors())
        result = []
        mult_input_button = self.element_is_visible(self.locators.MULTIPLE_COLOR_INPUT)
        for i in range(3):
            mult_input_button.send_keys(color[i])
            mult_input_button.send_keys(Keys.ENTER)
            result.append(self.elements_are_visible(self.locators.MULTI_INPUT_RESULT)[i].text)
        return color, result

    @allure.step("Remove certain colors from input")
    def remove_each_colors(self) -> str:
        for i in range(3):
            self.element_is_visible(self.locators.DELETE_ONE_COLOR).click()
        try:
            return self.element_is_visible(self.locators.MULTI_INPUT_RESULT).text
        except TimeoutException:
            return "Multiple color input is empty"

    @allure.step("Remove all colors from intput")
    def remove_all_colors(self) -> str:
        self.element_is_visible(self.locators.DELETE_ALL_COLORS).click()
        try:
            return self.element_is_visible(self.locators.MULTI_INPUT_RESULT).text
        except TimeoutException:
            return "Multiple color input is empty"

    @allure.step("Fill single color input")
    def fill_single_color_input(self) -> tuple[str, str]:
        color = random.choice(next(generated_colors()))
        self.element_is_visible(self.locators.SINGLE_COLOR_INPUT).send_keys(color)
        self.element_is_visible(self.locators.SINGLE_COLOR_INPUT).send_keys(Keys.ENTER)
        return color, self.element_is_visible(self.locators.SINGLE_INPUT_RESULT).text

    @allure.step("Check multiple color input")
    def check_multiple_color_input(self) -> bool:
        input_color, result_color = self.fill_multiple_color_input()
        return input_color == result_color

    @allure.step("Check certain removing function")
    def check_certain_removing_function(self) -> str:
        self.fill_multiple_color_input()
        return self.remove_each_colors()

    @allure.step("Check all removing function")
    def check_all_removing_function(self) -> str:
        self.fill_multiple_color_input()
        return self.remove_all_colors()

    @allure.step("Check single color input")
    def check_single_color_input(self) -> bool:
        input_color, result_color = self.fill_single_color_input()
        return input_color == result_color


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    @allure.step("Set date at Simple Calendar")
    def set_date_and_return(self) -> tuple[str, str]:
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.INPUT_DATE)
        previous_date = input_date.get_attribute("value")
        input_date.click()
        with allure.step("Set Month"):
            self.set_item_by_text(self.locators.SELECT_MONTH, date.month)
        with allure.step("Set Year"):
            self.set_item_by_text(self.locators.SELECT_YEAR, date.year)
        with allure.step("Set Day"):
            self.set_item_from_date_list(self.locators.SELECT_DAY, str(int(date.day)))
        result_date = input_date.get_attribute("value")
        return previous_date, result_date

    @allure.step("Set date at Time Calendar")
    def set_time_date_and_return(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.TIME_DATE_INPUT)
        previous_date = input_date.get_attribute("value")
        input_date.click()
        with allure.step("Set Month"):
            self.element_is_visible(self.locators.TIME_DATE_MONTH_DROP).click()
            self.set_item_from_date_list(self.locators.TIME_DATE_SELECT_MONTH, date.month)
        with allure.step("Set Year"):
            self.element_is_visible(self.locators.TIME_DATE_YEAR_DROP).click()
            self.set_year_for_time_date_picker(self.locators.TIME_DATE_SELECT_YEAR, date.year)
        with allure.step("Set Day"):
            self.set_item_from_date_list(self.locators.SELECT_DAY, date.day)
        with allure.step("Set Time"):
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

    def set_year_for_time_date_picker(self, element, value):  # метод для неправильного календаря
        item_list = self.elements_are_visible(element)
        while True:
            item = item_list[1]
            if item.text == value:
                item.click()
                break
            else:
                self.element_is_visible(self.locators.TIME_DATE_YEAR_SEARCH_OLD).click()
                item_list = self.elements_are_visible(element)


class SliderPage(BasePage):
    locators = SliderPageLocators()

    @allure.step("Move Slider")
    def change_slider_position_and_get_position(self) -> tuple[str, str, str]:
        slider_point = self.element_is_visible(locator=self.locators.INPUT_SLIDER)
        slider_value = self.element_is_visible(locator=self.locators.SLIDER_VALUE)
        previous_value = slider_value.get_attribute(name="value")
        self.action_drag_and_drop_by_offset(element=slider_point, x_coards=random.randint(0, 100), y_coards=0)
        result_value = slider_value.get_attribute(name="value")
        return previous_value, result_value, slider_point.get_attribute(name="value")


class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators()

    @allure.step("Run Progress Bar")
    def run_progress_and_return_values(self) -> tuple[str, str, str]:
        start_stop_button = self.element_is_visible(self.locators.START_STOP_BUTTON)
        progress_bar = self.element_is_present(self.locators.PROGRESS_BAR)
        previous_value = progress_bar.get_attribute("aria-valuenow")
        with allure.step("Start progress"):
            start_stop_button.click()
        time.sleep(2)
        second_value = progress_bar.get_attribute("aria-valuenow")
        time.sleep(2)
        final_value = progress_bar.get_attribute("aria-valuenow")
        time.sleep(6)
        return previous_value, second_value, final_value

    @allure.step("Reset progress")
    def reset_progress_and_return_value(self) -> str:
        progress_bar = self.element_is_present(self.locators.PROGRESS_BAR)
        with allure.step("Reset progress"):
            self.element_is_visible(self.locators.RESET_BUTTON).click()
        reset_value = progress_bar.get_attribute("aria-valuenow")
        return reset_value

    @allure.step("Check progress bar")
    def check_progress_bar(self) -> bool:
        previous_value, second_value, final_value = self.run_progress_and_return_values()
        return previous_value < second_value < final_value

    @allure.step("Check reset function")
    def check_reset_function(self) -> bool:
        reset_value = self.reset_progress_and_return_value()
        return reset_value == "0"


class TabsPage(BasePage):
    locators = TabsPageLocators()

    @allure.step("Read Tabs content")
    def get_tabs_texts(self) -> list:
        tabs_locators_dictic = {0: self.locators.WHAT_TAB,
                                1: self.locators.ORIGIN_TAB,
                                2: self.locators.USE_TAB,
                                3: self.locators.MORE_TAB}
        text_locators_dictic = {0: self.locators.WHAT_TEXT,
                                1: self.locators.ORIGIN_TEXT,
                                2: self.locators.USE_TEXT,
                                3: self.locators.MORE_TEXT}
        tabs_texts = []
        for i in range(4):
            try:
                tabs_texts.append(len(self.element_is_visible(text_locators_dictic[i]).text))
            except TimeoutException:
                try:
                    self.element_is_visible(tabs_locators_dictic[i]).click()
                    tabs_texts.append(len(self.element_is_visible(text_locators_dictic[i]).text))
                except ElementClickInterceptedException or TimeoutException:
                    print(f"\nASSERTION! Element <{tabs_locators_dictic[i][1]}> of Tabs Page isn't clickable or element"
                          f" <{text_locators_dictic[i][1]}> of Tabs Page isn't visible")
        return tabs_texts

    @allure.step("Check tabs content")
    def check_tabs_content(self):
        tabs_content = self.get_tabs_texts()
        if len(tabs_content) == 4:
            if tabs_content[0] != 574:
                return False, "WHAT_TAB text different for expected"
            if tabs_content[1] != 763:
                return False, "ORIGIN_TAB text different for expected"
            if tabs_content[2] != 613:
                return False, "USE_TAB text different for expected"
            if tabs_content[3] != 452:
                return False, "MORE_TAB text different for expected"
        else:
            return False, "Not all element's has been added"
        return True, "Test Passed"


class ToolTipsPage(BasePage):
    locators = ToolTipsPageLocators()

    @allure.step("Read all tips")
    def get_text_from_tips(self):
        dictic = {0: self.locators.BUTTON, 1: self.locators.FIELD, 2: self.locators.CONTRARY, 3: self.locators.DATE}
        tip = self.locators.TIP
        result_dictic = {}
        with allure.step("Hover element and append content"):
            for i in range(4):
                try:
                    self.action_hover(self.element_is_visible(dictic[i]))
                    key = self.element_is_visible(dictic[i]).get_attribute("aria-describedby")
                    value = self.element_is_visible(tip).text
                    result_dictic[key] = value
                except TimeoutException:
                    print(f"\nError with <{dictic[i][1]}> element of Tool Tips Page")
        return result_dictic

    @allure.step("Check tips content")
    def check_tips_content(self):
        tips_content = self.get_text_from_tips()
        return len(tips_content) == 4


class MenuPage(BasePage):
    locators = MenuPageLocators()

    @allure.step("Hover all menu tabs")
    def hover_all_menu_tabs_and_get_text(self) -> list:
        elements_list = self.elements_are_present(self.locators.ALL_ELEMENTS)
        result = []
        for item in elements_list:
            self.action_hover(item)
            result.append(item.text)
        return result

    @allure.step("Read all tabs on the way to element")
    def choose_menu_tab(self, tab):
        dictic = {"Main Item 1": self.locators.MAIN_ITEM_1, "Main Item 2": self.locators.MAIN_ITEM_2,
                  "Sub Item 1": self.locators.SUB_ITEM_1, "Sub Item 2": self.locators.SUB_ITEM_2,
                  "SUB SUB LIST »": self.locators.SUB_LIST, "Sub Sub Item 1": self.locators.SUB_SUB_ITEM_1,
                  "Sub Sub Item 2": self.locators.SUB_SUB_ITEM_2, "Main Item 3": self.locators.MAIN_ITEM_3}
        with allure.step(f"Read all tabs on the way to {tab}"):
            if tab == "Main Item 1" or tab == "Main Item 2" or tab == "Main Item 3":
                self.element_is_visible(dictic[tab]).click()
            if tab == "Sub Item 1" or tab == "Sub Item 2" or tab == "SUB SUB LIST »":
                self.action_hover(self.element_is_visible(dictic["Main Item 2"]))
                self.element_is_visible(dictic[tab]).click()
            if tab == "Sub Sub Item 1" or tab == "Sub Sub Item 2":
                self.action_hover(self.element_is_visible(dictic["Main Item 2"]))
                self.action_hover(self.element_is_visible(dictic["SUB SUB LIST »"]))
                self.element_is_visible(dictic[tab]).click()
        tab_name = self.element_is_visible(dictic[tab]).text
        return tab, tab_name

    @allure.step("Check drop all tabs")
    def check_hover_all_tabs(self):
        result = self.hover_all_menu_tabs_and_get_text()
        return len(result) == 8


class SelectMenuPage(BasePage):
    locators = SelectMenuPageLocators()

    @allure.step("Select Value")
    def select_value(self):
        self.element_is_visible(self.locators.SELECT_VALUE).click()
        element = random.choice(self.elements_are_visible(self.locators.SELECT_VALUE_DROPDOWN))
        try:
            element.click()
        except ElementClickInterceptedException:
            print("\n --ERROR-- Element moving when it shouldn't")

    @allure.step("Select Title")
    def select_title(self):
        self.element_is_visible(self.locators.SELECT_TITLE).click()
        element = random.choice(self.elements_are_visible(self.locators.SELECT_TITLE_DROPDOWN))
        try:
            element.click()
        except ElementClickInterceptedException:
            print("\n --ERROR-- Element moving when it shouldn't")

    @allure.step("Select colors at 'Multiselect Dropdown'")
    def select_colors(self):
        self.go_to_element(self.element_is_visible(self.locators.SELECT_COLORS))
        self.element_is_visible(self.locators.SELECT_COLORS).click()
        elements = self.elements_are_visible(self.locators.SELECT_COLORS_DROPDOWN)
        time.sleep(1)
        with allure.step("Select colors"):
            for element in elements:
                self.go_to_element(element)
                element.click()

    @allure.step("Remove colors from 'Multiselect Dropdown'")
    def remove_colors(self):
        with allure.step("Remove certain colors"):
            for _ in range(2):
                self.element_is_visible(self.locators.REMOVE_COLOR).click()
                time.sleep(0.5)
            self.element_is_visible(self.locators.GET_COLOR_VALUE).click()

    @allure.step("Check 'Select Value'")
    def check_select_value(self):
        self.remove_element()
        self.select_value()
        try:
            return bool(self.element_is_visible(self.locators.GET_VALUE_CONTENT).text)  # возврат True если есть контент
        except TimeoutException:
            return False

    @allure.step("Check 'Select Title'")
    def check_select_title(self):
        self.select_title()
        try:
            return bool(self.element_is_visible(self.locators.GET_TITLE_CONTENT))  # возврат True если есть контент
        except TimeoutException:
            return False

    @allure.step("Check Selecting 'Select Colors' function")
    def check_selecting_select_colors(self):
        self.select_colors()
        try:
            return len(self.elements_are_visible(self.locators.GET_COLOR_VALUE)) == 4
        except TimeoutException:
            return False

    @allure.step("Check Removing 'Select Colors' function")
    def check_removing_select_colors(self):
        self.remove_colors()
        try:
            return len(self.elements_are_visible(self.locators.GET_COLOR_VALUE)) == 2
        except TimeoutException:
            return False
