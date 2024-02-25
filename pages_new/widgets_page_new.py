import random
import time

import allure
from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from elements.buttons import Button
from elements.input_fields import InputField
from elements.title import Title
from generator.generator import generated_colors, generated_date
from pages.base_page import BasePage
from locators.widgets_page_locators import (AccordianPageLocators as APLocators,
                                            AutoCompletePageLocators as ACPLocators,
                                            DatePickerPageLocators as DPPLocators,
                                            SliderPageLocators as SPLocators,
                                            ProgressBarPageLocators as PBPLocators,
                                            TabsPageLocators as TPLocators,
                                            ToolTipsPageLocators as TTPLocators,
                                            MenuPageLocators as MPLocators,
                                            SelectMenuPageLocators as SMPLocators)


class AccordiansPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, url="https://demoqa.com/accordian")

        self.wili_accord = Button(driver=driver,
                                  locator=APLocators.WHATISLOREMIPSUM_ACCORD)
        self.wili_title = Title(driver=driver,
                                locator=APLocators.WHATISLOREMIPSUM_TEXT)
        self.wdicf_accord = Button(driver=driver,
                                   locator=APLocators.WHATDOESITCOMEFROM_ACCORD)
        self.wdicf_title = Title(driver=driver,
                                 locator=APLocators.WHATDOESITCOMEFROM_TEXT)
        self.wdwui_accord = Button(driver=driver,
                                   locator=APLocators.WHYDOWEUSEIT_ACCORD)
        self.wdwui_title = Title(driver=driver,
                                 locator=APLocators.WHYDOWEUSEIT_TEXT)

    @allure.step("Get chosen accord content")
    def get_chosen_accord_text(self, accord: str) -> str:
        accords_dictic = {"wili": self.wili_accord,
                          "wdicf": self.wdicf_accord,
                          "wdwui": self.wdwui_accord}
        title_dictic = {"wili": self.wili_title,

                        "wdicf": self.wdicf_title,
                        "wdwui": self.wdwui_title}
        try:
            self.go_to_element(title_dictic[accord].is_visible())
            return title_dictic[accord].is_visible().text
        except TimeoutException:
            self.go_to_element(accords_dictic[accord].is_visible())
            accords_dictic[accord].is_visible().click()
            return title_dictic[accord].is_visible().text


class AutoCompletePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, url="https://demoqa.com/auto-complete")

        self.multiple_color_input = InputField(driver=driver,
                                               locator=ACPLocators.MULTIPLE_COLOR_INPUT)
        self.multiple_color_result = Title(driver=driver,
                                           locator=ACPLocators.MULTI_INPUT_RESULT)
        self.delete_certain_color = Button(driver=driver,
                                           locator=ACPLocators.DELETE_ONE_COLOR)
        self.delete_all_colors = Button(driver=driver,
                                        locator=ACPLocators.DELETE_ALL_COLORS)
        self.single_color_input = InputField(driver=driver,
                                             locator=ACPLocators.SINGLE_COLOR_INPUT)
        self.single_color_result = Title(driver=driver,
                                         locator=ACPLocators.SINGLE_INPUT_RESULT)

    @allure.step("Fill multiple color input")
    def fill_multiple_color_input(self) -> tuple[list[str], list[str]]:
        color = next(generated_colors())
        result = []
        for i in range(3):
            self.multiple_color_input.is_visible().send_keys(color[i])
            self.multiple_color_input.is_visible().send_keys(Keys.ENTER)
            result.append(self.multiple_color_result.are_visible()[i].text)
        return color, result

    @allure.step("Remove certain colors from input")
    def remove_each_colors(self) -> str:
        colors_count = len(self.multiple_color_result.are_visible())
        for _ in range(colors_count):
            self.delete_certain_color.is_visible().click()
        try:
            return self.multiple_color_result.is_visible().text
        except TimeoutException:
            return "Multiple color input is empty"

    @allure.step("Remove all colors from input")
    def remove_all_colors(self) -> str:
        self.delete_all_colors.is_visible().click()
        try:
            return self.multiple_color_result.is_visible().text
        except TimeoutException:
            return "Multiple color input is empty"

    @allure.step("Fill single color input")
    def fill_single_color_input(self) -> tuple[str, str]:
        color = random.choice(next(generated_colors()))
        self.single_color_input.is_visible().send_keys(color)
        self.single_color_input.is_visible().send_keys(Keys.ENTER)
        return color, self.single_color_result.is_visible().text

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
    def __init__(self, driver):
        super().__init__(driver=driver, url="https://demoqa.com/date-picker")

        self.input_date = InputField(driver=driver, locator=DPPLocators.INPUT_DATE)
        self.select_month = Button(driver=driver, locator=DPPLocators.SELECT_MONTH)
        self.select_year = Button(driver=driver, locator=DPPLocators.SELECT_YEAR)
        self.select_day = Button(driver=driver, locator=DPPLocators.SELECT_DAY)
        self.time_date_input = InputField(driver=driver,
                                          locator=DPPLocators.TIME_DATE_INPUT)
        self.time_date_month_drop = InputField(driver=driver,
                                               locator=DPPLocators.TIME_DATE_MONTH_DROP)
        self.time_date_select_month = Button(driver=driver,
                                             locator=DPPLocators.TIME_DATE_SELECT_MONTH)
        self.time_date_year_drop = InputField(driver=driver,
                                              locator=DPPLocators.TIME_DATE_YEAR_DROP)
        self.time_date_select_year = Button(driver=driver,
                                            locator=DPPLocators.TIME_DATE_SELECT_YEAR)
        self.time_date_select_time = Button(driver=driver,
                                            locator=DPPLocators.TIME_DATE_SELECT_TIME)
        self.time_date_search_old_year = Button(driver=driver,
                                                locator=DPPLocators.TIME_DATE_YEAR_SEARCH_OLD)

    @allure.step("Set date at Simple Calendar")
    def set_date_and_return(self) -> tuple[str, str]:
        date = next(generated_date())
        previous_date = self.input_date.is_visible().get_attribute("value")
        self.input_date.is_visible().click()
        with allure.step("Set Month"):
            self.set_item_by_text(self.select_month, date.month)
        with allure.step("Set Year"):
            self.set_item_by_text(self.select_year, date.year)
        with allure.step("Set Day"):
            self.set_item_from_date_list(self.select_day, str(int(date.day)))
        result_date = self.input_date.is_visible().get_attribute("value")
        return previous_date, result_date

    @allure.step("Set date at Time Calendar")
    def set_time_date_and_return(self) -> tuple[str, str]:
        date = next(generated_date())
        previous_date = self.time_date_input.is_visible().get_attribute("value")
        self.time_date_input.is_visible().click()
        with allure.step("Set Month"):
            self.time_date_month_drop.is_visible().click()
            self.set_item_from_date_list(self.time_date_select_month, date.month)
        with allure.step("Set Year"):
            self.time_date_year_drop.is_visible().click()
            self.set_year_for_time_date_picker(self.time_date_select_year, date.year)
        with allure.step("Set Day"):
            self.set_item_from_date_list(self.select_day, date.day)
        with allure.step("Set Time"):
            self.set_item_from_date_list(self.time_date_select_time, date.time)
        result_date = self.time_date_input.is_visible().get_attribute("value")
        return previous_date, result_date

    @staticmethod
    def set_item_by_text(element, value):
        select = Select(element.is_present())
        select.select_by_visible_text(value)

    @staticmethod
    def set_item_from_date_list(element: Button, value: str):
        item_list = element.are_visible()
        for item in item_list:
            if item.text == value:
                item.click()
                break

    @allure.step("Set year for TimeDate picker")
    def set_year_for_time_date_picker(self, element: Button, value: str):
        item_list = element.are_present()
        while True:
            item = item_list[1]
            if item.text == value:
                item.click()
                break
            else:
                self.time_date_search_old_year.is_visible().click()
                item_list = element.are_visible()


class SliderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, url="https://demoqa.com/slider")

        self.slider_dot = Button(driver=driver, locator=SPLocators.INPUT_SLIDER)
        self.slider_value = Title(driver=driver, locator=SPLocators.SLIDER_VALUE)

    @allure.step("Move Slider")
    def change_slider_position_and_get_position(self) -> tuple[str, str, str]:
        previous_value = self.slider_value.is_visible().get_attribute(name="value")
        self.action_drag_and_drop_by_offset(element=self.slider_dot.is_visible(),
                                            x_coards=random.randint(0, 100), y_coards=0)
        result_value = self.slider_value.is_visible().get_attribute(name="value")
        return (previous_value, result_value,
                self.slider_dot.is_visible().get_attribute(name="value"))


class ProgressBarPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, url="https://demoqa.com/progress-bar")

        self.start_stop_button = Button(driver=driver,
                                        locator=PBPLocators.START_STOP_BUTTON)
        self.progress_bar = Title(driver=driver,
                                  locator=PBPLocators.PROGRESS_BAR)
        self.reset_button = Button(driver=driver,
                                   locator=PBPLocators.RESET_BUTTON)

    @allure.step("Run Progress Bar")
    def run_progress_bar_and_return_values(self) -> tuple[str, str, str, str]:
        previous_value = self.progress_bar.is_present().get_attribute(name="aria-valuenow")
        with allure.step("Start Progress"):
            self.start_stop_button.is_visible().click()
        time.sleep(2)
        self.start_stop_button.is_visible().click()
        second_value = self.progress_bar.is_visible().get_attribute(name="aria-valuenow")
        time.sleep(1)
        paused_value = self.progress_bar.is_visible().get_attribute(name="aria-valuenow")
        self.start_stop_button.is_visible().click()
        time.sleep(2)
        final_value = self.progress_bar.is_visible().get_attribute(name="aria-valuenow")
        time.sleep(6)
        return previous_value, second_value, paused_value, final_value

    @allure.step("Reset Progress")
    def reset_progress_and_return_value(self) -> str:
        with allure.step("Reset Progress"):
            self.reset_button.is_visible().click()
        reset_value = self.progress_bar.is_present().get_attribute(name="aria-valuenow")
        return reset_value

    @allure.step("Check progress bar")
    def check_progress_bar(self) -> bool:
        previous_value, second_value, paused_value, final_value = (
            self.run_progress_bar_and_return_values())
        return previous_value < second_value < final_value and second_value == paused_value

    @allure.step("Check reset button")
    def check_reset_button(self) -> bool:
        reset_value = self.reset_progress_and_return_value()
        return reset_value == "0"


class TabsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, url="https://demoqa.com/tabs")

        self.what_tab = Button(driver=driver, locator=TPLocators.WHAT_TAB)
        self.what_text = Title(driver=driver, locator=TPLocators.WHAT_TEXT)
        self.origin_tab = Button(driver=driver, locator=TPLocators.ORIGIN_TAB)
        self.origin_text = Title(driver=driver, locator=TPLocators.ORIGIN_TEXT)
        self.use_tab = Button(driver=driver, locator=TPLocators.USE_TAB)
        self.use_text = Title(driver=driver, locator=TPLocators.USE_TEXT)
        self.more_tab = Button(driver=driver, locator=TPLocators.MORE_TAB)
        self.more_text = Title(driver=driver, locator=TPLocators.MORE_TEXT)

    @allure.step("Read Tabs content")
    def get_tabs_text(self) -> list:
        dictic = {0: [self.what_tab, self.what_text], 1: [self.origin_tab, self.origin_text],
                  2: [self.use_tab, self.use_text], 3: [self.more_tab, self.more_text]}
        tabs_content = []
        for i in range(4):
            try:
                dictic[i][0].is_visible().click()
                tabs_content.append(len(dictic[i][1].is_visible().text))
            except ElementClickInterceptedException:
                print(f"\nASSERTION! Element <{dictic[i][0]}> "
                      f"of Tabs Page hasn't been clicked or element"
                      f"<{dictic[i][1]} of Tabs Page isn't visible> ")
        return tabs_content

    @allure.step("Check tabs content")
    def check_tabs_content(self) -> tuple[bool, str]:
        tabs_content = self.get_tabs_text()
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
    def __init__(self, driver):
        super().__init__(driver=driver, url="https://demoqa.com/tool-tips")

        self.hover_me_button = Button(driver=driver, locator=TTPLocators.BUTTON)
        self.hover_me_field = InputField(driver=driver, locator=TTPLocators.FIELD)
        self.hover_me_contrary = Title(driver=driver, locator=TTPLocators.CONTRARY)
        self.hover_me_date = Title(driver=driver, locator=TTPLocators.DATE)
        self.tip = Title(driver=driver, locator=TTPLocators.TIP)

    @allure.step("Read all tips")
    def get_text_from_tips(self) -> list:
        elements = [self.hover_me_button, self.hover_me_field, self.hover_me_contrary, self.hover_me_date]
        result_list = []
        with allure.step("Hover element and append content"):
            for element in elements:
                try:
                    self.go_to_element(element=element.is_visible())
                    self.action_hover(element=element.is_visible())
                    time.sleep(0.5)
                    result_list.append(self.tip.is_visible().text)
                except TimeoutException:
                    print(f"\nError with <{element}> element of Tool Tips Page")
        return result_list

    @allure.step("Check tips content")
    def check_tips_content(self) -> bool:
        expected_tips = ["You hovered over the Button", "You hovered over the text field",
                         "You hovered over the Contrary", "You hovered over the 1.10.32"]
        for tip, expected_tip in dict(zip(self.get_text_from_tips(), expected_tips)).items():
            if tip != expected_tip:
                return False
        return True


class MenuPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, url="https://demoqa.com/menu#")

        self.all_tabs = Button(driver=driver, locator=MPLocators.ALL_ELEMENTS)
        self.main_item1 = Button(driver=driver, locator=MPLocators.MAIN_ITEM_1)
        self.main_item2 = Button(driver=driver, locator=MPLocators.MAIN_ITEM_2)
        self.sub_item1 = Button(driver=driver, locator=MPLocators.SUB_ITEM_1)
        self.sub_item2 = Button(driver=driver, locator=MPLocators.SUB_ITEM_2)
        self.sub_sub_list = Button(driver=driver, locator=MPLocators.SUB_LIST)
        self.sub_sub_item1 = Button(driver=driver, locator=MPLocators.SUB_SUB_ITEM_1)
        self.sub_sub_item2 = Button(driver=driver, locator=MPLocators.SUB_SUB_ITEM_2)
        self.main_item3 = Button(driver=driver, locator=MPLocators.MAIN_ITEM_3)

    @allure.step("Hover all menu tabs")
    def hover_all_menu_tabs_and_get_text(self) -> list:
        tabs_list = self.all_tabs.are_present()
        result = []
        for tab in tabs_list:
            self.action_hover(element=tab)
            result.append(tab.text)
        return result


    @allure.step("Read chosen tab")
    def chose_menu_tab_and_return_text(self, tab: str) -> tuple[str, str]:
        dictic = {"Main Item 1": self.main_item1, "Main Item 2": self.main_item2,
                  "Sub Item 1": self.sub_item1, "Sub Item 2": self.sub_item2,
                  "SUB SUB LIST »": self.sub_sub_list, "Sub Sub Item 1": self.sub_sub_item1,
                  "Sub Sub Item 2": self.sub_sub_item2, "Main Item 3": self.main_item3}
        with allure.step(f"Get tab text"):
            if tab == "Main Item 1" or tab == "Main Item 2" or tab == "Main Item 3":
                dictic[tab].is_visible().click()
                return tab, dictic[tab].is_visible().text
            if tab == "Sub Item 1" or tab == "Sub Item 2" or tab == "SUB SUB LIST »":
                self.action_hover(element=self.main_item2.is_visible())
                dictic[tab].is_visible().click()
                return tab, dictic[tab].is_visible().text
            if tab == "Sub Sub Item 1" or tab == "Sub Sub Item 2":
                self.action_hover(element=self.main_item2.is_visible())
                self.action_hover(element=self.sub_sub_list.is_visible())
                dictic[tab].is_visible().click()
                return tab, dictic[tab].is_visible().text

    @allure.step("Check drop all tabs")
    def check_hovering_all_tabs(self) -> bool:
        result = self.hover_all_menu_tabs_and_get_text()
        return len(result) == len(self.all_tabs.are_present())


class SelectMenuPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, url="https://demoqa.com/select-menu")

        self.select_value_field = InputField(driver=driver,
                                             locator=SMPLocators.SELECT_VALUE)
        self.select_value_values = Title(driver=driver,
                                         locator=SMPLocators.SELECT_VALUE_DROPDOWN)
        self.value_content = Title(driver=driver,
                                   locator=SMPLocators.GET_VALUE_CONTENT)
        self.select_title_field = InputField(driver=driver,
                                             locator=SMPLocators.SELECT_TITLE)
        self.select_title_values = Title(driver=driver,
                                         locator=SMPLocators.SELECT_TITLE_DROPDOWN)
        self.title_content = Title(driver=driver,
                                   locator=SMPLocators.GET_TITLE_CONTENT)
        self.select_colors_field = InputField(driver=driver,
                                              locator=SMPLocators.SELECT_COLORS)
        self.select_colors_values = Title(driver=driver,
                                          locator=SMPLocators.SELECT_COLORS_DROPDOWN)
        self.certain_remove_colors = Button(driver=driver,
                                            locator=SMPLocators.REMOVE_COLOR)
        self.color_content = Title(driver=driver,
                                   locator=SMPLocators.GET_COLOR_VALUE)

    @allure.step("Select and return selected value")
    def select_and_return_value(self) -> str:
        self.select_value_field.is_visible().click()
        value = random.choice(self.select_value_values.are_visible())
        try:
            value_text = value.text
            value.click()
            return value_text
        except ElementClickInterceptedException:
            print("\n --ERROR-- Element moving when it shouldn't")

    @allure.step("Select and return selected title")
    def select_and_return_title(self) -> str:
        self.select_title_field.is_visible().click()
        title = random.choice(self.select_title_values.are_visible())
        try:
            title_text = title.text
            title.click()
            return title_text
        except ElementClickInterceptedException:
            print("\n --ERROR-- Element moving when it shouldn't")

    @allure.step("Select and return selected colors")
    def select_and_return_colors(self) -> list[str]:
        self.go_to_element(element=self.select_colors_field.is_visible())
        self.select_colors_field.is_visible().click()
        colors = random.sample(population=self.select_colors_values.are_visible(), k=3)
        selected_colors = []
        with allure.step("Select colors"):
            for color in colors:
                self.go_to_element(element=color)
                try:
                    selected_colors.append(color.text)
                    color.click()
                except ElementClickInterceptedException:
                    print("\n --ERROR-- Element moving when it shouldn't")
        return selected_colors  # вернуть список с выбранными цветами

    @allure.step("Remove certain colors and return one left")
    def remove_certain_colors_and_return_left(self) -> tuple[str, str]:
        previous_selected_colors = self.color_content.are_visible()
        colors_to_remove = random.sample(population=previous_selected_colors, k=2)
        for color in colors_to_remove:  # Удалить каждый выбранный элемент по своей кнопке удаления
            self.element_is_visible(locator=(By.XPATH,
                                    f"//*[contains(text(), '{color.text}')]/following-sibling::div")).click()
            previous_selected_colors.pop(previous_selected_colors.index(color))
        return previous_selected_colors[0].text, self.color_content.is_visible().text   # вернуть оставшийся в списке и оставшийся в поле ввода элемент

    @allure.step("Check 'Select Value' Field")
    def check_select_value(self) -> bool:
        self.remove_element()
        selected_value = self.select_and_return_value()
        return selected_value == self.value_content.is_visible().text

    @allure.step("Check 'Select Title' Field")
    def check_select_title(self) -> bool:
        selected_title = self.select_and_return_title()
        return selected_title == self.title_content.is_visible().text

    @allure.step("Check 'Select Colors' Field")
    def check_select_colors(self) -> bool:
        selected_colors = self.select_and_return_colors()
        colors_field_content = [color.text for color in self.color_content.are_visible()]
        for color in selected_colors:
            if color not in colors_field_content:
                return False
        return True

    @allure.step("Check Removing colors function")
    def check_removing_colors_function(self) -> bool:
        previous_left_color, last_color = self.remove_certain_colors_and_return_left()
        return previous_left_color == last_color
