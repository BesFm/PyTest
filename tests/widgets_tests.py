from conftest import driver
from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, \
    ToolTipsPage, MenuPage, SelectMenuPage
import random


class TestWidgets:

    class TestAccordian:

        def test_accordians(self, driver):
            accordians_page = AccordianPage(driver, "https://demoqa.com/accordian")
            accordians_page.open()
            first_accord_text = accordians_page.get_wili_accord_text()
            second_accord_text = accordians_page.get_wdicf_accord_text()
            third_accord_text = accordians_page.get_wdwui_accord_text()
            assert first_accord_text is not None, "First accordian content difference from expected or not founded"
            assert second_accord_text is not None, "Second accordian content difference from expected or not founded"
            assert third_accord_text is not None, "Third accordian content difference from expected or not founded"

    class TestAutoComplete:

        def test_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            mult_input_colors, mult_input_result = autocomplete_page.fill_multiple_color_input()
            if random.randint(1, 2) == 2:                               # случайно генерируем способ удаления
                mult_remove_result = autocomplete_page.remove_each_colors_from_input()
            else:
                mult_remove_result = autocomplete_page.remove_all_colors_from_input()
            single_input_colors, single_input_result = autocomplete_page.fill_single_color_input()
            assert mult_input_colors == mult_input_result, "Result colors difference from input colors"
            assert mult_remove_result is None, "Colors isn,t removed"
            assert single_input_colors == single_input_result, "Result colors difference from input colors"

    class TestDataPicker:

        def test_date_picker(self, driver):
            date_picker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
            date_picker_page.open()
            input_date, output_date = date_picker_page.set_date()
            assert input_date != output_date, "Date hasn't changed"

        def test_time_date_picker(self, driver):
            date_picker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
            date_picker_page.open()
            input_date, output_date = date_picker_page.set_time_date()
            assert input_date != output_date, "Date hasn't changed"

    class TestSlider:

        def test_slider(self, driver):
            slider_page = SliderPage(driver, "https://demoqa.com/slider")
            slider_page.open()
            previous_value, result_value, slider_own_value = slider_page.change_slider_position()
            assert previous_value != result_value, "Slider hasn't change position"
            assert result_value == slider_own_value, "Have difference between result value and slider value"

    class TestProgressBar:

        def test_progress_bar(self, driver):
            progress_bar_page = ProgressBarPage(driver, "https://demoqa.com/progress-bar")
            progress_bar_page.open()
            first_value, second_value, final_value, reset_value = progress_bar_page.run_progress()
            assert reset_value == first_value and reset_value == "0", ("Reset button didn't"
                                                                       " work or progress isn't finished")
            assert first_value < second_value < final_value, "Start/Stop button didn't work"

    class TestTabsPage:

        def test_tabs(self, driver):
            tabs_page = TabsPage(driver, "https://demoqa.com/tabs")
            tabs_page.open()
            result_list = tabs_page.get_tabs_texts()
            assert len(result_list) == 4, "Not all element's was added"
            assert result_list[0] == 574, "WHAT_TAB text different for expected"
            assert result_list[1] == 763, "ORIGIN_TAB text different for expected"
            assert result_list[2] == 613, "USE_TAB text different for expected"
            assert result_list[3] == 452, "MORE_TAB text different for expected"

    class TestToolTipsPage:

        def test_tool_tips(self, driver):
            tool_tips_page = ToolTipsPage(driver, "https://demoqa.com/tool-tips")
            tool_tips_page.open()
            elements_dictic = tool_tips_page.get_text_from_tips()
            assert len(elements_dictic) == 4, "Not all elements was added"

    class TestMenuPage:

        def test_menu_page(self, driver):
            menu_page = MenuPage(driver, "https://demoqa.com/menu#")
            menu_page.open()
            result = menu_page.hover_all_menu_tabs()
            tab_name_chosen, tab_name_clicked = menu_page.choose_menu_tab("SUB SUB LIST »")
            assert len(result) == 8, "Result list isn't full"
            assert tab_name_chosen == tab_name_clicked, "Chosen another tab"

    class TestSelectMenuPage:

        def test_select_menu(self, driver):
            select_menu_page = SelectMenuPage(driver, "https://demoqa.com/select-menu")
            select_menu_page.open()
            select_menu_page.select_value()
            value, title = select_menu_page.select_title()
            select_menu_page.select_old_color()
            color = select_menu_page.select_colors()
            select_menu_page.select_old_car()
            assert value is not False, "Value isn't chosen"
            assert title is not False, "Title isn't chosen"
            assert color is not False, "Color isn't chosen"
