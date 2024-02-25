import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from conftest import driver

from pages_new.widgets_page_new import AccordiansPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, \
    TabsPage, ToolTipsPage, MenuPage, SelectMenuPage


@allure.suite("Test Widgets")
class TestWidgets:
    @allure.feature("Test Accordian")
    class TestAccordian:

        @allure.title("Check accordians content")
        def test_accordians_content(self, driver: WebDriver):
            accordians_page = AccordiansPage(driver=driver)
            accordians_page.open()
            assert accordians_page.get_chosen_accord_text("wili") is not None, \
                "First accordian content difference from expected or not founded"
            assert accordians_page.get_chosen_accord_text("wdicf") is not None, \
                "Second accordian content difference from expected or not founded"
            assert accordians_page.get_chosen_accord_text("wdwui") is not None, \
                "Third accordian content difference from expected or not founded"

    @allure.feature("Test Auto Complete")
    class TestAutoComplete:

        @allure.title("Test multiple autocomplete - select colors")
        def test_multiple_autocomplete_select(self, driver: WebDriver):
            autocomplete_page = AutoCompletePage(driver=driver)
            autocomplete_page.open()
            assert autocomplete_page.check_multiple_color_input(), "Result colors difference from expected"

        @allure.title("Test multiple autocomplete - certain remove")
        def test_multiple_autocomplete_certain_remove(self, driver: WebDriver):
            autocomplete_page = AutoCompletePage(driver=driver)
            autocomplete_page.open()
            assert autocomplete_page.check_certain_removing_function() == "Multiple color input is empty", \
                "Colors hasn't been removed"

        @allure.title("Test multiple autocomplete - all remove")
        def test_multiple_autocomplete_all_remove(self, driver: WebDriver):
            autocomplete_page = AutoCompletePage(driver=driver)
            autocomplete_page.open()
            assert autocomplete_page.check_all_removing_function() == "Multiple color input is empty", \
                "Colors hasn't been removed"

        @allure.title("Test single autocomplete - select color")
        def test_single_autocomplete_select(self, driver: WebDriver):
            autocomplete_page = AutoCompletePage(driver=driver)
            autocomplete_page.open()
            assert autocomplete_page.check_single_color_input(), "Result colors difference from input colors"

    @allure.feature("Test Calendar")
    class TestDataPicker:

        @allure.title("Test Simple Calendar")
        def test_date_picker(self, driver: WebDriver):
            date_picker_page = DatePickerPage(driver=driver)
            date_picker_page.open()
            input_date, output_date = date_picker_page.set_date_and_return()
            assert input_date != output_date, "Date hasn't been changed"

        @allure.title("Test Time Date Calendar")
        def test_time_date_picker(self, driver: WebDriver):
            date_picker_page = DatePickerPage(driver=driver)
            date_picker_page.open()
            input_date, output_date = date_picker_page.set_time_date_and_return()
            assert input_date != output_date, "Date hasn't been changed"

    @allure.feature("Test Slider")
    class TestSlider:

        @allure.title("Change slider position and get value")
        def test_slider(self, driver: WebDriver):
            slider_page = SliderPage(driver=driver)
            slider_page.open()
            previous_value, result_value, displayed_value = slider_page.change_slider_position_and_get_position()
            assert previous_value != result_value, "Slider position hasn't been changed"
            assert result_value == displayed_value, "Displayed value difference from expected"

    @allure.feature("Test Progress Bar")
    class TestProgressBar:

        @allure.title("Test Progress Bar")
        def test_progress_bar(self, driver: WebDriver):
            progress_bar_page = ProgressBarPage(driver=driver)
            progress_bar_page.open()
            assert progress_bar_page.check_progress_bar(), "Start/Stop button isn't work"
            assert progress_bar_page.check_reset_button(), "Reset button isn't work or progress hasn't been finished"


    @allure.feature("Test Tabs")
    class TestTabs:

        @allure.title("Check tabs content")
        def test_tabs(self, driver: WebDriver):
            tabs_page = TabsPage(driver=driver)
            tabs_page.open()
            result, message = tabs_page.check_tabs_content()
            assert result, message


    @allure.feature("Test Tool Tips")
    class TestToolTips:

        @allure.title("Test all tips")
        def test_tool_tips(self, driver: WebDriver):
            tool_tips_page = ToolTipsPage(driver=driver)
            tool_tips_page.open()
            assert tool_tips_page.check_tips_content(), "Some of the tips contain unexpected text"

    @allure.feature("Test Menu Tabs")
    class TestMenuTabs:

        @allure.title("Test hover all tabs")
        def test_hover_all_tabs(self, driver: WebDriver):
            menu_page = MenuPage(driver=driver)
            menu_page.open()
            assert menu_page.check_hovering_all_tabs(), "Some of tab hasn't been added to result list"

        @allure.title("Test chosen tab")
        def test_select_tab(self, driver: WebDriver):
            menu_page = MenuPage(driver=driver)
            menu_page.open()
            chosen_tab, clicked_tab = menu_page.chose_menu_tab_and_return_text(tab="SUB SUB LIST »")
            assert chosen_tab == clicked_tab, "Clicked tab text difference from chosen"


    @allure.feature("Test Select Menu")
    class TestSelectMenu:

        @allure.title("Test value and title field")
        def test_value_and_title_field(self, driver: WebDriver):
            select_menu_page = SelectMenuPage(driver=driver)
            select_menu_page.open()
            assert select_menu_page.check_select_value(), "Chosen value difference from displayed"
            assert select_menu_page.check_select_title(), "Chosen title difference from displayed"

        @allure.title("Test multiselect color field")
        def test_multiselect_color_field(self, driver: WebDriver):
            select_menu_page = SelectMenuPage(driver=driver)
            select_menu_page.open()
            assert select_menu_page.check_select_colors(), "Selected colors difference from expected"
            assert select_menu_page.check_removing_colors_function(), "Colors hasn't been removed"
