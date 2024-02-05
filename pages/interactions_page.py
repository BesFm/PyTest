import random
import time

from pages.base_page import BasePage
from locators.interactions_page_locators import (SortablePageLocators, SelectablePageLocators, ResizablePageLocators,
                                                 DroppablePageLocators)


def convert_sortable_list(elements_list):
    converted_list = elements_list
    for i in range(len(converted_list)):
        converted_list[i] = converted_list[i].text
    return converted_list


class SortablePage(BasePage):
    locators = SortablePageLocators()

    def change_elements_positions(self):
        tab_listik = [self.locators.GRID_TAB, self.locators.LIST_TAB]
        elements_listik = [self.locators.GRID_ELEMENTS, self.locators.LIST_ELEMENTS]
        unsorted_converted_list = []
        sorted_converted_list = []
        for i in range(2):
            self.element_is_visible(tab_listik[i]).click()
            unsorted_list = self.elements_are_visible(elements_listik[i])
            unsorted_converted_list.append(convert_sortable_list(self.elements_are_visible(elements_listik[i])))
            source, target = random.sample(unsorted_list, 2)
            self.action_drag_and_drop_to(source, target)
            sorted_converted_list.append(convert_sortable_list(self.elements_are_visible(elements_listik[i])))
        return unsorted_converted_list, sorted_converted_list


class SelectablePage(BasePage):
    locators = SelectablePageLocators()

    def select_elements(self, page):
        tab_listik = {"list": self.locators.LIST_TAB, "grid": self.locators.GRID_TAB}
        elements_listik = {"list": self.locators.LIST_ELEMENTS, "grid": self.locators.GRID_ELEMENTS}
        selected_elements = []
        approved_elements = []
        self.element_is_visible(tab_listik[page]).click()
        unselected_elements = self.elements_are_visible(elements_listik[page])
        chosen_elements = random.sample(unselected_elements, 3)
        for element in chosen_elements:
            element.click()
            selected_elements.append(element.text)
            approved_elements.append(element.get_attribute("class"))
        return selected_elements, all(map(lambda x: "active" in x, approved_elements))


class ResizablePage(BasePage):
    locators = ResizablePageLocators()

    def remove_footer(self):
        self.remove_element()

    def resize_window(self, window):
        dictic = {"box window": [self.locators.RESIZABLE_BOX_WINDOW, self.locators.RESIZABLE_BOX_ARROW],
                  "simple window": [self.locators.RESIZABLE_WINDOW, self.locators.RESIZABLE_ARROW]}
        element = self.element_is_visible(dictic[window][0])
        self.go_to_element(element)
        first_params = tuple(self.get_width_height_window(element))
        self.action_drag_and_drop_by_offset(self.element_is_present(dictic[window][1]),
                                            random.randint(1, 300), random.randint(1, 300))
        second_params = tuple(self.get_width_height_window(element))
        self.action_drag_and_drop_by_offset(self.element_is_present(dictic[window][1]),
                                            random.randint(-300, -1), random.randint(-300, -1))
        final_params = tuple(self.get_width_height_window(element))
        return first_params, second_params, final_params

    def get_width_height_window(self, element):
        width, height = element.get_attribute("style").split("; ")
        return int(width.split(":")[1].strip("px")), int(height.split(":")[1].strip("px;"))


class DroppablePage(BasePage):
    locators = DroppablePageLocators()

    def move_simple_box(self):
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        simple_moving_box = self.element_is_visible(self.locators.SIMPLE_MOVING_BOX)
        simple_target_box = self.element_is_visible(self.locators.SIMPLE_TARGET_BOX)
        self.action_drag_and_drop_to(simple_moving_box, simple_target_box)
        return simple_target_box.text

    def move_acceptable_box(self):
        self.element_is_visible(self.locators.ACCEPTABLE_TAB).click()
        notacceptable_moving_box = self.element_is_visible(self.locators.NOTACCEPTABLE_MOVING_BOX)
        acceptable_moving_box = self.element_is_visible(self.locators.ACCEPTABLE_MOVING_BOX)
        acceptable_target_box = self.element_is_visible(self.locators.ACCEPT_TARGET_BOX)
        self.action_drag_and_drop_to(notacceptable_moving_box, acceptable_target_box)
        not_accept_result = acceptable_target_box.text
        self.action_drag_and_drop_to(acceptable_moving_box, acceptable_target_box)
        accept_result = acceptable_target_box.text
        return not_accept_result, accept_result

    def move_greedy_box(self):
        self.element_is_visible(self.locators.GREEDY_TAB).click()
        greedy_moving_box = self.element_is_visible(self.locators.GREEDY_MOVING_BOX)
        inner_notgreedy_target_box = self.element_is_visible(self.locators.INNER_NOTGREEDY_TARGET)
        outer_notgreedy_target_box = self.element_is_visible(self.locators.OUTER_NOTGREEDY_TARGET)
        inner_greedy_target_box = self.element_is_visible(self.locators.INNER_GREEDY_TARGET)
        outer_greedy_target_box = self.element_is_visible(self.locators.OUTER_GREEDY_TARGET)
        self.action_drag_and_drop_to(greedy_moving_box, inner_notgreedy_target_box)
        notgreedy_outer_result = outer_notgreedy_target_box.text.strip()
        self.action_drag_and_drop_to(greedy_moving_box, inner_greedy_target_box)
        greedy_outer_result_1 = outer_greedy_target_box.text.strip()
        time.sleep(1)
        self.action_drag_and_drop_by_offset(greedy_moving_box, 100, 0)
        greedy_outer_result_2 = outer_greedy_target_box.text.strip()
        return notgreedy_outer_result.split("\n"), greedy_outer_result_1.split("\n"), greedy_outer_result_2.split("\n")

    def move_revertable_box(self, move_type="will revert"):
        self.element_is_visible(self.locators.REVERT_TAB).click()
        time.sleep(1)
        types_dictic = {"will revert": self.locators.REVERTABLE_MOVING_BOX,
                        "not revert": self.locators.NONREVERTABLE_MOVING_BOX}
        moving_box = self.element_is_visible(types_dictic[move_type])
        revertable_target_box = self.element_is_visible(self.locators.REVERTABLE_TARGET_BOX)
        self.action_drag_and_drop_to(moving_box, revertable_target_box)
        result_target_text = revertable_target_box.text
        time.sleep(1)
        if move_type == "will revert":
            moving_assignment = moving_box.get_attribute("style") == "position: relative; left: 0px; top: 0px;"
        else:
            moving_assignment = moving_box.get_attribute("style") != "position: relative; left: 0px; top: 0px;"
        print(moving_box.get_attribute("style"))
        return result_target_text, moving_assignment
