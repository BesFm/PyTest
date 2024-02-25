import allure

from conftest import driver
from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, \
    ToolTipsPage, MenuPage, SelectMenuPage


@allure.suite("Test Widgets")
class TestWidgets:
    @allure.feature("Test Accordian")
    class TestAccordian:

        @allure.title("Check accordians content")
        def test_accordians(self, driver):
            accordians_page = AccordianPage(driver, "https://demoqa.com/accordian")
            accordians_page.open()
            assert accordians_page.get_wili_accord_text() is not None, \
                "First accordian content difference from expected or not founded"
            assert accordians_page.get_wdicf_accord_text() is not None, \
                "Second accordian content difference from expected or not founded"
            assert accordians_page.get_wdwui_accord_text() is not None, \
                "Third accordian content difference from expected or not founded"

    @allure.feature("Test Auto Complete")
    class TestAutoComplete:

        @allure.title("Test multiple autocomplete - select colors")
        def test_multiple_autocomplete_select(self, driver):
            autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            assert autocomplete_page.check_multiple_color_input(), "Result colors difference from input colors"

        @allure.title("Test multiple autocomplete - certain remove")
        def test_multiple_autocomplete_certain_remove(self, driver):
            autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            assert autocomplete_page.check_certain_removing_function() == "Multiple color input is empty", \
                "Colors hasn't been removed"

        @allure.title("Test multiple autocomplete - all remove")
        def test_multiple_autocomplete_all_remove(self, driver):
            autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            assert autocomplete_page.check_all_removing_function() == "Multiple color input is empty", \
                "Colors hasn't been removed"

        @allure.title("Test single autocomplete - select color")
        def test_single_autocomplete_select(self, driver):
            autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            assert autocomplete_page.check_single_color_input(), "Result colors difference from input colors"

    @allure.feature("Test Calendar")
    class TestDataPicker:

        @allure.title("Test Simple Calendar")
        def test_date_picker(self, driver):
            date_picker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
            date_picker_page.open()
            input_date, output_date = date_picker_page.set_date_and_return()
            assert input_date != output_date, "Date hasn't changed"

        @allure.title("Test Time Calendar")
        def test_time_date_picker(self, driver):
            date_picker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
            date_picker_page.open()
            input_date, output_date = date_picker_page.set_time_date_and_return()
            assert input_date != output_date, "Date hasn't changed"

    @allure.feature("Test Slider")
    class TestSlider:

        @allure.title("Check Slider")
        def test_slider(self, driver):
            slider_page = SliderPage(driver, "https://demoqa.com/slider")
            slider_page.open()
            previous_value, result_value, slider_own_value = slider_page.change_slider_position_and_get_position()
            assert previous_value != result_value, "Slider hasn't change position"
            assert result_value == slider_own_value, "Have difference between result value and slider value"

    @allure.feature("Test Progress Bar")
    class TestProgressBar:

        @allure.title("Check Progress Bar")
        def test_progress_bar(self, driver):
            progress_bar_page = ProgressBarPage(driver, "https://demoqa.com/progress-bar")
            progress_bar_page.open()
            assert progress_bar_page.check_progress_bar(), "Start/Stop button didn't work"
            assert progress_bar_page.check_reset_function(), ("Reset button didn't"
                                                              " work or progress isn't finished")

    @allure.feature("Test Tabs")
    class TestTabs:

        @allure.title("Check Tabs content")
        def test_tabs(self, driver):
            tabs_page = TabsPage(driver, "https://demoqa.com/tabs")
            tabs_page.open()
            result, message = tabs_page.check_tabs_content()
            assert result, message

    @allure.feature("Test Tool Tips")
    class TestToolTips:

        @allure.title("Check count all tips")
        def test_tool_tips(self, driver):
            tool_tips_page = ToolTipsPage(driver, "https://demoqa.com/tool-tips")
            tool_tips_page.open()
            assert tool_tips_page.check_tips_content(), "Not all elements was added"

    @allure.feature("Test Menu")
    class TestMenu:

        @allure.title("Test hover all tabs")
        def test_hover_all_tabs(self, driver):
            menu_page = MenuPage(driver, "https://demoqa.com/menu#")
            menu_page.open()
            assert menu_page.check_hover_all_tabs(), "Result list isn't full"

        @allure.title("Test chosen tab")
        def test_select_tab(self, driver):
            menu_page = MenuPage(driver, "https://demoqa.com/menu#")
            menu_page.open()
            tab_name_chosen, tab_name_clicked = menu_page.choose_menu_tab(tab="SUB SUB LIST »")
            assert tab_name_chosen == tab_name_clicked, "Chosen another tab"

    @allure.feature("Test Select Menu")
    class TestSelectMenu:

        @allure.title("Check Select Menu")
        def test_select_menu(self, driver):
            select_menu_page = SelectMenuPage(driver, "https://demoqa.com/select-menu")
            select_menu_page.open()
            assert select_menu_page.check_select_value(), "Value isn't chosen"
            assert select_menu_page.check_select_title(), "Title isn't chosen"
            assert select_menu_page.check_selecting_select_colors(), "Not all colors has been selected"
            assert select_menu_page.check_removing_select_colors(), "Colors isn't removed"
