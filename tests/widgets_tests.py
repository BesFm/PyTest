from conftest import driver
from pages.widgets_page import AccordianPage, AutoCompletePage
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
