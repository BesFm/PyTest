import random

from pages.base_page import BasePage
from locators.interactions_page_locators import SortablePageLocators


class SortablePage(BasePage):
    locators = SortablePageLocators()

    def convert_sortable_list(self, elements_list):
        converted_list = elements_list
        for i in range(len(converted_list)):
            converted_list[i] = converted_list[i].text
        return converted_list

    def change_elements_positions(self):
        tab_listik = [self.locators.GRID_TAB, self.locators.LIST_TAB]
        elements_listik = [self.locators.GRID_ELEMENTS, self.locators.LIST_ELEMENTS]
        unsorted_converted_list = []
        sorted_converted_list = []
        for i in range(2):
            self.element_is_visible(tab_listik[i]).click()
            unsorted_list = self.elements_are_visible(elements_listik[i])
            unsorted_converted_list.append(self.convert_sortable_list(self.elements_are_visible(elements_listik[i])))
            source, target = random.sample(unsorted_list, 2)
            self.action_drag_and_drop_to(source, target)
            sorted_converted_list.append(self.convert_sortable_list(self.elements_are_visible(elements_listik[i])))
        return unsorted_converted_list, sorted_converted_list

