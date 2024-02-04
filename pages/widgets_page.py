import random
import time

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


class SliderPage(BasePage):
    locators = SliderPageLocators()

    def change_slider_position(self):
        slider_point = self.element_is_visible(self.locators.INPUT_SLIDER)
        slider_value = self.element_is_visible(self.locators.SLIDER_VALUE)
        previous_value = slider_value.get_attribute("value")
        self.action_drag_and_drop_by_offset(slider_point, random.randint(0, 100), 0)
        result_value = slider_value.get_attribute("value")
        return previous_value, result_value, slider_point.get_attribute("value")


class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators()

    def run_progress(self):
        start_stop_button = self.element_is_visible(self.locators.START_STOP_BUTTON)
        progress_bar = self.element_is_present(self.locators.PROGRESS_BAR)
        previous_value = progress_bar.get_attribute("aria-valuenow")
        start_stop_button.click()
        time.sleep(2)
        second_value = progress_bar.get_attribute("aria-valuenow")
        time.sleep(2)
        final_value = progress_bar.get_attribute("aria-valuenow")
        time.sleep(6)
        self.element_is_visible(self.locators.RESET_BUTTON).click()
        reset_value = progress_bar.get_attribute("aria-valuenow")
        return previous_value, second_value, final_value, reset_value


class TabsPage(BasePage):
    locators = TabsPageLocators()

    def get_tabs_texts(self):
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
                    print(f"!ASSERTION! Element {tabs_locators_dictic[i][1]} of Tabs Page isn't clickable or element"
                          f" {text_locators_dictic[i][1]} of Tabs Page isn't visible")
        return tabs_texts


class ToolTipsPage(BasePage):
    locators = ToolTipsPageLocators()

    def get_text_from_tips(self):
        dictic = {0: self.locators.BUTTON, 1: self.locators.FIELD, 2: self.locators.CONTRARY, 3: self.locators.DATE}
        tip = self.locators.TIP
        result_dictic = {}
        for i in range(4):
            try:
                self.action_move_to(self.element_is_visible(dictic[i]))
                time.sleep(0.5)
                self.element_is_visible(tip)
                key = self.element_is_visible(dictic[i]).get_attribute("aria-describedby")
                value = self.element_is_visible(tip).text
                result_dictic[key] = value
            except TimeoutException:
                print()
                print(f"Error with {dictic[i][1]} element of Tool Tips Page")
        return result_dictic


class MenuPage(BasePage):
    locators = MenuPageLocators()

    def hover_all_menu_tabs(self):
        elements_list = self.elements_are_present(self.locators.ALL_ELEMENTS)
        result = []
        for item in elements_list:
            self.action_move_to(item)
            result.append(item.text)
        return result

    def choose_menu_tab(self, tab):
        dictic = {"Main Item 1": self.locators.MAIN_ITEM_1, "Main Item 2": self.locators.MAIN_ITEM_2,
                  "Sub Item 1": self.locators.SUB_ITEM_1, "Sub Item 2": self.locators.SUB_ITEM_2,
                  "SUB SUB LIST »": self.locators.SUB_LIST, "Sub Sub Item 1": self.locators.SUB_SUB_ITEM_1,
                  "Sub Sub Item 2": self.locators.SUB_SUB_ITEM_2, "Main Item 3": self.locators.MAIN_ITEM_3}
        if tab == "Main Item 1" or tab == "Main Item 2" or tab == "Main Item 3":
            self.element_is_visible(dictic[tab]).click()
        if tab == "Sub Item 1" or tab == "Sub Item 2" or tab == "SUB SUB LIST »":
            self.action_move_to(self.element_is_visible(dictic["Main Item 2"]))
            self.element_is_visible(dictic[tab]).click()
        if tab == "Sub Sub Item 1" or tab == "Sub Sub Item 2":
            self.action_move_to(self.element_is_visible(dictic["Main Item 2"]))
            self.action_move_to(self.element_is_visible(dictic["SUB SUB LIST »"]))
            self.element_is_visible(dictic[tab]).click()
        tab_name = self.element_is_visible(dictic[tab]).text
        return tab, tab_name


class SelectMenuPage(BasePage):
    locators = SelectMenuPageLocators()

    def select_value(self):
        self.element_is_visible(self.locators.SELECT_VALUE).click()
        element = random.choice(self.elements_are_visible(self.locators.SELECT_VALUE_DROPDOWN))
        element.click()

    def select_title(self):
        self.element_is_visible(self.locators.SELECT_TITLE).click()
        element = random.choice(self.elements_are_visible(self.locators.SELECT_TITLE_DROPDOWN))
        element.click()
        return self.elements_are_visible(self.locators.GET_VALUE_TITLE)     # возвращаем значения полей value и title

    def select_old_color(self):
        self.element_is_visible(self.locators.SELECT_OLD_COLOR).click()
        element = random.choice(self.elements_are_visible(self.locators.SELECT_OLD_COLOR_DROPDOWN))
        element.click()

    def select_colors(self):
        self.element_is_visible(self.locators.SELECT_COLORS).click()
        elements = self.elements_are_visible(self.locators.SELECT_COLORS_DROPDOWN)
        time.sleep(1)
        for element in elements:
            self.go_to_element(element)
            element.click()
        for _ in range(2):
            self.element_is_visible(self.locators.REMOVE_COLORS).click()
            time.sleep(0.5)
        self.element_is_present(self.locators.GET_COLOR_VALUE).click()
        return self.element_is_visible(self.locators.GET_COLOR_VALUE).text

    def select_old_car(self):           # плохой дропдаун
        self.element_is_visible(self.locators.SELECT_OLD_CAR).click()
        element = random.choice(self.elements_are_visible(self.locators.SELECT_OLD_CAR_DROPDOWN))
        element.click()
