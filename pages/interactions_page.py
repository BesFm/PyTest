import random
import time
import re

import allure
from selenium.common import MoveTargetOutOfBoundsException, JavascriptException

from pages.base_page import BasePage
from locators.interactions_page_locators import (SortablePageLocators,
                                                 SelectablePageLocators,
                                                 ResizablePageLocators,
                                                 DroppablePageLocators,
                                                 DraggablePageLocators)


class SortablePage(BasePage):
    locators = SortablePageLocators()

    @allure.step("Change elements positions and return previous and final list")
    def sort_elements_and_get_previous_and_final_list(self, tab: str) -> tuple[
        list, list]:
        tab_dictic = {"grid": self.locators.GRID_TAB, "list": self.locators.LIST_TAB}
        elements_dictic = {"grid": self.locators.GRID_ELEMENTS,
                           "list": self.locators.LIST_ELEMENTS}
        with allure.step("Sort elements"):
            self.element_is_visible(tab_dictic[tab]).click()
            unsorted_list = self.elements_are_visible(elements_dictic[tab])
            self.go_to_element(unsorted_list[-1])
            unsorted_converted_list = [element.text for element in unsorted_list]
            source, target = random.sample(unsorted_list, 2)
            self.action_drag_and_drop_to(source, target)
            sorted_converted_list = [element.text for element in
                                     self.elements_are_visible(elements_dictic[tab])]
        return unsorted_converted_list, sorted_converted_list

    @allure.step("Check element's sorting ")
    def check_elements_sorting(self, tab: str) -> bool:
        unsorted_list, sorted_list = self.sort_elements_and_get_previous_and_final_list(
            tab)
        return unsorted_list != sorted_list


class SelectablePage(BasePage):
    locators = SelectablePageLocators()

    @allure.step("Select elements and return elements and attributes")
    def select_and_return_elements_and_attributes(self, page: str) -> tuple[list, list]:
        tab_dictic = {"list": self.locators.LIST_TAB, "grid": self.locators.GRID_TAB}
        elements_dictic = {"list": self.locators.LIST_ELEMENTS,
                           "grid": self.locators.GRID_ELEMENTS}
        selected_elements = []
        approved_elements = []
        self.element_is_visible(tab_dictic[page]).click()
        unselected_elements = self.elements_are_visible(elements_dictic[page])
        chosen_elements = random.sample(unselected_elements, 3)
        with allure.step(f"Select chosen elements at {page} tab"):
            for element in chosen_elements:
                element.click()
                selected_elements.append(element.text)
                approved_elements.append(element.get_attribute("class"))
        return selected_elements, list(map(lambda x: "active" in x, approved_elements))

    @allure.step("Check selected elements")
    def check_selected_elements(self, page: str) -> bool:
        selected_el, approved_el = self.select_and_return_elements_and_attributes(
            page)
        return (len(selected_el) == len(approved_el) == 3 and
                all(approved_el))


class ResizablePage(BasePage):
    locators = ResizablePageLocators()

    @allure.step("Resize window")
    def resize_window_and_get_params(self, window) -> tuple:
        dictic = {"box window": [self.locators.RESIZABLE_BOX_WINDOW,
                                 self.locators.RESIZABLE_BOX_ARROW],
                  "simple window": [self.locators.RESIZABLE_WINDOW,
                                    self.locators.RESIZABLE_ARROW]}
        element = self.element_is_visible(dictic[window][0])
        self.go_to_element(element)
        first_params = tuple(self.get_width_height_window(element))
        with allure.step(f"Resizing {window}"):
            # увеличить размеры окна
            self.action_drag_and_drop_by_offset(
                self.element_is_present(dictic[window][1]),
                random.randint(1, 350), random.randint(1, 350))
            time.sleep(0.5)
            second_params = tuple(self.get_width_height_window(element))
            # уменьшить размеры окна
            self.action_drag_and_drop_by_offset(
                self.element_is_present(dictic[window][1]),
                random.randint(-350, -1), random.randint(-350, -1))
        time.sleep(0.5)
        final_params = tuple(self.get_width_height_window(element))
        return first_params, second_params, final_params

    @staticmethod
    def get_width_height_window(element) -> tuple[int, int]:
        width, height = re.findall(r"\d[0-9]\d", element.get_attribute("style"))
        return int(width), int(height)

    @allure.step("Check resizing of box window")
    def check_resizing_of_box_window(self) -> bool | tuple[bool, str]:
        self.remove_element()
        first_params, second_params, final_params = self.resize_window_and_get_params(
            "box window")
        if second_params[0] >= 500 and second_params[1] >= 300:
            return False, "Max window size has been exceeded"
        elif final_params[0] <= 150 and final_params[1] <= 150:
            return False, "Mix window size has been exceeded"
        elif first_params == second_params == final_params:
            return False, "Window size hasn't been changed"
        return True, "Test Passed"

    @allure.step("Check resizing")
    def check_resizing_of_simple_window(self) -> bool:
        self.remove_element()
        first_params, second_params, final_params = self.resize_window_and_get_params(
            "simple window")
        return first_params != second_params != final_params


class DroppablePage(BasePage):
    locators = DroppablePageLocators()

    @allure.step("Moving element at simple tab")
    def move_simple_box(self) -> str:
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        simple_moving_box = self.element_is_visible(self.locators.SIMPLE_MOVING_BOX)
        simple_target_box = self.element_is_visible(self.locators.SIMPLE_TARGET_BOX)
        self.action_drag_and_drop_to(simple_moving_box, simple_target_box)
        return simple_target_box.text

    @allure.step("Moving element at accept tab")
    def move_acceptable_box(self) -> tuple[str, str]:
        self.element_is_visible(self.locators.ACCEPTABLE_TAB).click()
        notacceptable_moving_box = self.element_is_visible(
            self.locators.NOTACCEPTABLE_MOVING_BOX)
        acceptable_moving_box = self.element_is_visible(
            self.locators.ACCEPTABLE_MOVING_BOX)
        acceptable_target_box = self.element_is_visible(self.locators.ACCEPT_TARGET_BOX)
        with allure.step("Move notacceptable element to target"):
            self.action_drag_and_drop_to(notacceptable_moving_box, acceptable_target_box)
        not_accept_result = acceptable_target_box.text
        with allure.step("Move acceptable element to target"):
            self.action_drag_and_drop_to(acceptable_moving_box, acceptable_target_box)
        accept_result = acceptable_target_box.text
        return not_accept_result, accept_result

    @allure.step("Moving element at prevent propagation tab - Not Greedy")
    def move_box_to_not_greedy_container(self) -> list:
        self.element_is_visible(self.locators.GREEDY_TAB).click()
        moving_box = self.element_is_visible(self.locators.GREEDY_MOVING_BOX)
        inner_notgreedy_target_box = self.element_is_visible(
            self.locators.INNER_NOTGREEDY_TARGET)
        outer_notgreedy_target_box = self.element_is_visible(
            self.locators.OUTER_NOTGREEDY_TARGET)
        with allure.step("Move element to small container"):
            self.action_drag_and_drop_to(moving_box, inner_notgreedy_target_box)
        notgreedy_outer_result = outer_notgreedy_target_box.text.strip()
        return notgreedy_outer_result.split("\n")

    @allure.step("Moving element at prevent propagation tab - Greedy")
    def move_box_to_greedy_container(self) -> tuple[list, list]:
        self.element_is_visible(self.locators.GREEDY_TAB).click()
        moving_box = self.element_is_visible(self.locators.GREEDY_MOVING_BOX)
        inner_greedy_target_box = self.element_is_visible(
            self.locators.INNER_GREEDY_TARGET)
        outer_greedy_target_box = self.element_is_visible(
            self.locators.OUTER_GREEDY_TARGET)
        with allure.step("Move element to small target"):
            self.action_drag_and_drop_to(moving_box, inner_greedy_target_box)
        greedy_outer_result_1 = outer_greedy_target_box.text.strip()
        with allure.step("Move element to large target"):
            self.action_drag_and_drop_by_offset(moving_box, x_coards=100, y_coards=0)
        greedy_outer_result_2 = outer_greedy_target_box.text.strip()
        return greedy_outer_result_1.split("\n"), greedy_outer_result_2.split("\n")

    @allure.step("Check moving to greedy container")
    def check_moving_to_greedy_container(self) -> tuple[bool, str]:
        self.remove_element()
        element_in_inner_container, element_in_outer_container = self.move_box_to_greedy_container()
        time.sleep(0.5)
        inner_react_previous, outer_react_previous = element_in_inner_container
        inner_react_final, outer_react_final = element_in_outer_container
        if inner_react_previous == outer_react_previous:
            return False, "One of the target isn't greedy while it should be"
        elif inner_react_final != outer_react_final:
            return False, "Element hasn't been moved to second target or target isn't react"
        return True, "Test Passed"

    @allure.step("Moving element at revert draggable tab")
    def move_revertable_box(self, move_type: str) -> tuple[str, bool]:
        self.element_is_visible(self.locators.REVERT_TAB).click()
        types_dictic = {"will revert": self.locators.REVERTABLE_MOVING_BOX,
                        "not revert": self.locators.NONREVERTABLE_MOVING_BOX}
        moving_box = self.element_is_visible(types_dictic[move_type])
        revertable_target_box = self.element_is_visible(
            self.locators.REVERTABLE_TARGET_BOX)
        with allure.step(f"Move {move_type} element to target"):
            self.action_drag_and_drop_to(moving_box, revertable_target_box)
        result_target_text = revertable_target_box.text
        time.sleep(1)
        if move_type == "will revert":
            moving_assignment = moving_box.get_attribute(
                "style") == "position: relative; left: 0px; top: 0px;"
        else:
            moving_assignment = moving_box.get_attribute(
                "style") != "position: relative; left: 0px; top: 0px;"
        return result_target_text, moving_assignment


class DraggablePage(BasePage):
    locators = DraggablePageLocators()

    @staticmethod
    def get_elements_position(element) -> tuple[int, int]:
        try:
            x_coord, y_coord = re.findall(r"\d[0-9]\d|\d[0-9]|\d",
                                          element.get_attribute("style"))
            return int(x_coord), int(y_coord)
        except ValueError:  # если кординаты не изменятся - в аттрибуте style не будет данных по паттерну
            return 0, 0

    @allure.step("Move element at Simple tab and return position")
    def move_simple_element_and_return_position(self) -> tuple:
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        moving_element = self.element_is_visible(self.locators.SIMPLE_MOVING_ELEMENT)
        previous_position = self.get_elements_position(
            moving_element)
        try:
            self.action_drag_and_drop_by_offset(moving_element, random.randint(1, 300),
                                                random.randint(1, 300))
            result_position = self.get_elements_position(
                moving_element)
        except MoveTargetOutOfBoundsException:
            result_position = self.get_elements_position(
                moving_element)
            return previous_position, result_position
        return previous_position, result_position

    @allure.step("Check moving simple element")
    def check_moving_simple_element(self) -> bool:
        previous_position, result_position = self.move_simple_element_and_return_position()
        return previous_position != result_position

    @allure.step("Move Axis Restricted element")
    def move_axis_element_and_return_position(self, element: str) -> tuple:
        self.element_is_visible(self.locators.AXIS_RESTRICTED_TAB).click()
        elements_dictic = {"x_element": self.locators.X_MOVING_ELEMENT,
                           "y_element": self.locators.Y_MOVING_ELEMENT}
        moving_element = self.element_is_visible(elements_dictic[element])
        self.go_to_element(moving_element)
        previous_position = self.get_elements_position(moving_element)
        with allure.step("Move Axis element"):
            try:  # изменить положение элемента
                self.action_drag_and_drop_by_offset(moving_element,
                                                    random.randint(1, 600),
                                                    random.randint(1, 100))
                result_position = self.get_elements_position(moving_element)
            except MoveTargetOutOfBoundsException:
                result_position = self.get_elements_position(moving_element)
                return previous_position, result_position
        return previous_position, result_position

    @allure.step("Check moving Axis Restricted element")
    def check_moving_axis_element(self, element: str) -> bool:
        try:
            self.remove_element()
        except JavascriptException:
            pass
        previous_position, result_position = self.move_axis_element_and_return_position(
            element=element)
        if element == "x_element":
            if result_position[
                1] != 0:  # проверить двигался ли элемент по недоступной для него оси
                return False
            else:
                return previous_position[0] != result_position[0]
        elif element == "y_element":
            if result_position[
                0] != 0:  # проверить двигался ли элемент по недоступной для него оси
                return False
            else:
                return previous_position[1] != result_position[1]

    @allure.step("Move Container Restricted element")
    def move_container_element_and_return_position(self,
                                                   element: str) -> tuple:
        self.element_is_visible(self.locators.CONTAINER_RESTRICTED_TAB).click()
        elements_dictic = {"box_contained": self.locators.BOX_MOVING_TEXT,
                           "parent_contained": self.locators.PARENT_MOVING_TEXT}
        moving_element = self.element_is_visible(elements_dictic[element])
        self.go_to_element(moving_element)
        previous_position = moving_element.get_attribute("style")
        with allure.step("Move Container element"):
            try:  # изменить положение элемента
                self.action_drag_and_drop_by_offset(moving_element,
                                                    random.randint(1, 600),
                                                    random.randint(1, 200))
                result_position = self.get_elements_position(moving_element)
            except MoveTargetOutOfBoundsException:
                result_position = self.get_elements_position(moving_element)
                return previous_position, result_position
        return previous_position, result_position

    @allure.step("Check moving Container Restricted element")
    def check_moving_container_element(self, element: str) -> bool:
        try:
            self.remove_element()
        except JavascriptException:
            pass
        previous_position, result_position = (
            self.move_container_element_and_return_position(element=element))
        if element == "box_contained":
            if result_position[0] > 655 or result_position[1] > 106:
                return False
        elif element == "parent_contained":
            if result_position[0] > 13 or result_position[1] > 86:
                return False
        return previous_position != result_position
