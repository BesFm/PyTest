import random
import re
import time
import allure
from selenium.common import TimeoutException, JavascriptException
from elements.buttons import Button
from elements.frame import Frame
from elements.moving_element import MovingElement
from elements.title import Title
from pages.base_page import BasePage
from locators.interactions_page_locators import (SortablePageLocators as SortLocators,
                                                 SelectablePageLocators as SelectLocators,
                                                 ResizablePageLocators as ResizeLocators,
                                                 DroppablePageLocators as DropLocators,
                                                 DraggablePageLocators as DragLocators)


class SortablePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, url="https://demoqa.com/sortable")

        self.grid_tab = Button(driver=driver, locator=SortLocators.GRID_TAB)
        self.list_tab = Button(driver=driver, locator=SortLocators.LIST_TAB)
        self.grid_elements = Title(driver=driver, locator=SortLocators.GRID_ELEMENTS)
        self.list_elements = Title(driver=driver, locator=SortLocators.LIST_ELEMENTS)

    @allure.step("Sort elements and return previous and final list")
    def sort_elements_and_get_unsorted_and_sorted_list(self, tab: str) -> tuple[list,
    list]:
        tab_dictic = {"grid": self.grid_tab, "list": self.list_tab}
        elements_dictic = {"grid": self.grid_elements, "list": self.list_elements}
        with allure.step("Sort elements"):
            tab_dictic[tab].is_visible().click()
            unsorted_list = elements_dictic[tab].are_visible()
            unsorted_converted_list = [element.text for element in unsorted_list]
            self.go_to_element(unsorted_list[-1])  # чтобы видеть все элементы
            source, target = random.sample(population=unsorted_list, k=2)
            self.action_drag_and_drop_to(source=source, target=target)
            sorted_list = elements_dictic[tab].are_visible()
            sorted_converted_list = [element.text for element in sorted_list]
        return unsorted_converted_list, sorted_converted_list

    @allure.step("Check element's sorting")
    def check_elements_sorting(self, tab: str) -> bool:
        unsorted_el, sorted_el = self.sort_elements_and_get_unsorted_and_sorted_list(
            tab=tab)
        return unsorted_el != sorted_el


class SelectablePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, url="https://demoqa.com/selectable")

        self.list_tab = Button(driver=driver, locator=SelectLocators.LIST_TAB)
        self.grid_tab = Button(driver=driver, locator=SelectLocators.GRID_TAB)
        self.list_elements = Title(driver=driver, locator=SelectLocators.LIST_ELEMENTS)
        self.grid_elements = Title(driver=driver, locator=SelectLocators.GRID_ELEMENTS)

    @allure.step("Select elements and return elements and attributes")
    def select_and_return_elements_and_attributes(self, tab: str) -> tuple[list, list]:
        tab_dictic = {"list": self.list_tab, "grid": self.grid_tab}
        elements_dictic = {"list": self.list_elements, "grid": self.grid_elements}
        selected_elements = []
        approved_elements = []
        tab_dictic[tab].is_visible().click()
        unselected_elements = elements_dictic[tab].are_visible()
        chosen_elements = random.sample(population=unselected_elements, k=3)
        with allure.step(f"Select chosen elements at {tab} tab"):
            for element in chosen_elements:
                element.click()
                selected_elements.append(element.text)
                approved_elements.append(element.get_attribute(name="class"))
        return selected_elements, approved_elements

    @allure.step("Check selected elements")
    def check_selected_elements(self, tab: str) -> bool:
        selected_el, approved_el = self.select_and_return_elements_and_attributes(tab=tab)
        approved_el = list(
            map(lambda x: "active" in x, approved_el))  # проверить активацию элемента
        return len(selected_el) == len(approved_el) == 3 and all(approved_el)


class ResizablePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, url="https://demoqa.com/resizable")

        self.resizable_box_window = Frame(driver=driver,
                                          locator=ResizeLocators.RESIZABLE_BOX_WINDOW)
        self.resizable_box_arrow = Button(driver=driver,
                                          locator=ResizeLocators.RESIZABLE_BOX_ARROW)
        self.resizable_window = Frame(driver=driver,
                                      locator=ResizeLocators.RESIZABLE_WINDOW)
        self.resizable_arrow = Button(driver=driver,
                                      locator=ResizeLocators.RESIZABLE_ARROW)

    @allure.step("Resize window")
    def resize_window_and_get_params(self, window: str) -> tuple:
        windows_dictic = {
            "box_window": [self.resizable_box_window, self.resizable_box_arrow],
            "simple_window": [self.resizable_window, self.resizable_arrow]}
        self.go_to_element(windows_dictic[window][0].is_visible())
        first_params = self.get_window_params(element=windows_dictic[window][0])
        with allure.step(f"Resizing of {window}"):
            # увеличить размеры окна
            self.action_drag_and_drop_by_offset(
                element=windows_dictic[window][1].is_visible(),
                x_coards=random.randint(a=1, b=350),
                y_coards=random.randint(a=1, b=350))
            time.sleep(0.5)
            second_params = self.get_window_params(element=windows_dictic[window][0])
            # уменьшить размеры окна
            self.action_drag_and_drop_by_offset(
                element=windows_dictic[window][1].is_visible(),
                x_coards=random.randint(a=-350, b=-1),
                y_coards=random.randint(a=-350, b=-1))
            time.sleep(0.5)
            final_params = self.get_window_params(element=windows_dictic[window][0])
            return first_params, second_params, final_params

    @staticmethod
    @allure.step("Get width and height of window")
    def get_window_params(element) -> tuple[int, int]:
        width, height = re.findall(pattern=r"\d[0-9]\d",
                                   string=element.is_visible().get_attribute("style"))
        return int(width), int(height)

    @allure.step("Check resizing of box window")
    def check_resizing_of_box_window(self) -> bool | tuple[bool, str]:
        self.remove_element()
        first_params, second_params, final_params = self.resize_window_and_get_params(
            window="box_window")
        if second_params[0] >= 500 and second_params[1] >= 300:
            return False, "Max window size has been exceeded"
        elif final_params[0] <= 150 and final_params[1] <= 150:
            return False, "Mix window size has been exceeded"
        elif first_params == second_params == final_params:
            return False, "Window size hasn't been changed"
        return True, "Test Passed"

    @allure.step("Check resizing of simple window")
    def check_resizing_of_simple_window(self) -> bool:
        self.remove_element()
        first_params, second_params, final_params = self.resize_window_and_get_params(
            window="simple_window")
        return first_params != second_params != final_params


class DroppablePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, url="https://demoqa.com/droppable")

        self.simple_tab = Button(driver=driver, locator=DropLocators.SIMPLE_TAB)
        self.simple_moving_box = MovingElement(driver=driver,
                                               locator=DropLocators.SIMPLE_MOVING_BOX)
        self.simple_target_box = Frame(driver=driver,
                                       locator=DropLocators.SIMPLE_TARGET_BOX)
        self.acceptable_tab = Button(driver=driver, locator=DropLocators.ACCEPTABLE_TAB)
        self.notacceptable_moving_box = MovingElement(driver=driver,
                                                      locator=DropLocators.NOTACCEPTABLE_MOVING_BOX)
        self.acceptable_moving_box = MovingElement(driver=driver,
                                                   locator=DropLocators.ACCEPTABLE_MOVING_BOX)
        self.acceptable_target_box = Frame(driver=driver,
                                           locator=DropLocators.ACCEPT_TARGET_BOX)
        self.greedy_tab = Button(driver=driver, locator=DropLocators.GREEDY_TAB)
        self.greedy_moving_box = MovingElement(driver=driver,
                                               locator=DropLocators.GREEDY_MOVING_BOX)
        self.inner_notgreedy_target = Frame(driver=driver,
                                            locator=DropLocators.INNER_NOTGREEDY_TARGET)
        self.outer_notgreedy_target = Frame(driver=driver,
                                            locator=DropLocators.OUTER_NOTGREEDY_TARGET)
        self.inner_greedy_target = Frame(driver=driver,
                                         locator=DropLocators.INNER_GREEDY_TARGET)
        self.outer_greedy_target = Frame(driver=driver,
                                         locator=DropLocators.OUTER_GREEDY_TARGET)
        self.revertable_tab = Button(driver=driver, locator=DropLocators.REVERT_TAB)
        self.revertable_moving_box = MovingElement(driver=driver,
                                                   locator=DropLocators.REVERTABLE_MOVING_BOX)
        self.nonrevertable_moving_box = MovingElement(driver=driver,
                                                      locator=DropLocators.NONREVERTABLE_MOVING_BOX)
        self.revertable_target_box = Frame(driver=driver,
                                           locator=DropLocators.REVERTABLE_TARGET_BOX)

    @allure.step("Move simple box")
    def move_simple_box_and_get_result(self) -> str:
        time.sleep(0.5)
        self.action_drag_and_drop_to(source=self.simple_moving_box.is_visible(),
                                     target=self.simple_target_box.is_visible())
        return self.simple_target_box.is_visible().text

    @allure.step("Moving not acceptable element to target")
    def move_not_acceptable_element_and_get_result(self) -> str:
        self.acceptable_tab.is_visible().click()
        self.action_drag_and_drop_to(source=self.notacceptable_moving_box.is_visible(),
                                     target=self.acceptable_target_box.is_visible())
        return self.acceptable_target_box.is_visible().text

    @allure.step("Moving acceptable element to target")
    def move_acceptable_element_and_get_result(self) -> str:
        self.acceptable_tab.is_visible().click()
        self.action_drag_and_drop_to(source=self.acceptable_moving_box.is_visible(),
                                     target=self.acceptable_target_box.is_visible())
        return self.acceptable_target_box.is_visible().text

    @allure.step("Moving element to NOT GREEDY target")
    def moving_element_to_not_greedy_target(self) -> tuple[str, str]:
        self.greedy_tab.is_visible().click()
        time.sleep(0.5)
        self.action_drag_and_drop_to(source=self.greedy_moving_box.is_visible(),
                                     target=self.inner_notgreedy_target.is_visible())
        common_result = self.outer_notgreedy_target.is_visible().text.strip()
        outer_target_result, inner_target_result = common_result.split("\n")
        return outer_target_result, inner_target_result

    @allure.step("Moving element to GREEDY target")
    def moving_element_to_greedy_target(self) -> tuple[str, str]:
        self.greedy_tab.is_visible().click()
        self.remove_element()
        time.sleep(0.5)
        self.action_drag_and_drop_to(source=self.greedy_moving_box.is_visible(),
                                     target=self.inner_greedy_target.is_visible())
        common_result = self.outer_notgreedy_target.is_visible().text.strip()
        outer_target_result, inner_target_result = common_result.split("\n")
        return outer_target_result, inner_target_result

    @allure.step("Moving element to EACH GREEDY targets")
    def moving_element_to_each_greedy_targets(self) -> tuple[str, str]:
        self.greedy_tab.is_visible().click()
        self.remove_element()
        self.action_drag_and_drop_to(source=self.greedy_moving_box.is_visible(),
                                     target=self.inner_greedy_target.is_visible())
        time.sleep(0.5)
        self.action_drag_and_drop_by_offset(element=self.greedy_moving_box.is_visible(),
                                            x_coards=100, y_coards=0)
        common_result = self.outer_greedy_target.is_visible().text.strip()
        outer_target_result, inner_target_result = common_result.split("\n")
        return outer_target_result, inner_target_result

    @allure.step("Move revertable element to target")
    def move_revertable_box(self) -> str:
        self.revertable_tab.is_visible().click()
        self.action_drag_and_drop_to(source=self.revertable_moving_box.is_visible(),
                                     target=self.revertable_target_box.is_visible())
        return self.revertable_moving_box.is_visible().get_attribute("style")

    @allure.step("Check moving revertable element")
    def check_moving_of_revertable_element(self) -> bool:
        position = self.move_revertable_box()
        return position == "position: relative; left: 0px; top: 0px;"

    @allure.step("Move non revertable element to target")
    def move_non_revertable_box(self) -> str:
        self.revertable_tab.is_visible().click()
        self.action_drag_and_drop_to(source=self.nonrevertable_moving_box.is_visible(),
                                     target=self.revertable_target_box.is_visible())
        return self.nonrevertable_moving_box.is_visible().get_attribute("style")

    @allure.step("Check moving non revertable element")
    def check_moving_of_non_revertable_element(self) -> bool:
        position = self.move_non_revertable_box()
        return position != "position: relative; left: 0px; top: 0px;"


class DraggablePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, url="https://demoqa.com/dragabble")

        self.simple_tab = Button(driver=driver, locator=DragLocators.SIMPLE_TAB)
        self.simple_moving_element = MovingElement(driver=driver,
                                                   locator=DragLocators.SIMPLE_MOVING_ELEMENT)
        self.axis_tab = Button(driver=driver, locator=DragLocators.AXIS_RESTRICTED_TAB)
        self.x_moving_element = MovingElement(driver=driver,
                                              locator=DragLocators.X_MOVING_ELEMENT)
        self.y_moving_element = MovingElement(driver=driver,
                                              locator=DragLocators.Y_MOVING_ELEMENT)
        self.container_tab = Button(driver=driver,
                                    locator=DragLocators.CONTAINER_RESTRICTED_TAB)
        self.box_moving_title = MovingElement(driver=driver,
                                              locator=DragLocators.BOX_MOVING_TEXT)
        self.parent_moving_title = MovingElement(driver=driver,
                                                 locator=DragLocators.PARENT_MOVING_TEXT)

    @staticmethod
    @allure.step("Get elements position")
    def get_element_position(element) -> tuple[int, int]:
        try:
            x_coord, y_coord = re.findall(r"\d[0-9]\d|\d[0-9]|\d",
                                          element.get_attribute("style"))
            return int(x_coord), int(y_coord)
        except ValueError:  # если координаты не изменятся - в атрибуте style не будет данных по паттерну
            return 0, 0

    @allure.step("Move element at simple tab and return position")
    def move_simple_element_and_return_position(self) -> tuple[tuple, tuple]:
        self.simple_tab.is_visible().click()
        previous_position = self.get_element_position(
            element=self.simple_moving_element.is_visible())
        try:
            self.action_drag_and_drop_by_offset(
                element=self.simple_moving_element.is_visible(),
                x_coards=random.randint(1, 300),
                y_coards=random.randint(1, 300))
            result_position = self.get_element_position(
                element=self.simple_moving_element.is_visible())
        except TimeoutException:
            result_position = self.get_element_position(
                element=self.simple_moving_element.is_visible())
            return previous_position, result_position
        return previous_position, result_position

    @allure.step("Check moving simple element")
    def check_moving_simple_element(self) -> bool:
        previous_position, result_position = self.move_simple_element_and_return_position()
        return previous_position != result_position

    @allure.step("Move Axis Restricted element")
    def move_axis_element_and_return_position(self, element: str) -> tuple:
        self.axis_tab.is_visible().click()
        elements_dictic = {"x_element": self.x_moving_element,
                           "y_element": self.y_moving_element}
        moving_element = elements_dictic[element].is_visible()
        previous_position = self.get_element_position(element=moving_element)
        with allure.step("Move Axis element"):
            try:
                self.action_drag_and_drop_by_offset(
                    element=elements_dictic[element].is_visible(),
                    x_coards=random.randint(1, 600),
                    y_coards=random.randint(1, 150))
                result_position = self.get_element_position(element=moving_element)
            except TimeoutException:
                result_position = self.get_element_position(element=moving_element)
                return previous_position, result_position
        return previous_position, result_position

    @allure.step("Check moving Axis Restricted element")
    def check_moving_axis_element(self, element: str) -> bool:
        try:
            self.remove_element()
        except JavascriptException:
            pass
        previous_position, result_position = (self.move_axis_element_and_return_position(
            element=element))
        if element == "x_element":
            if result_position[1] != 0:
                return False
            else:
                return previous_position[0] != result_position[0]
        elif element == "y_element":
            if result_position[0] != 0:
                return False
            else:
                return previous_position[1] != result_position[1]

    @allure.step("Move Container Restricted element")
    def move_container_element_and_return_position(self, element: str) -> tuple:
        self.container_tab.is_visible().click()
        elements_dictic = {"box_contained": self.box_moving_title,
                           "parent_contained": self.parent_moving_title}
        moving_element = elements_dictic[element].is_visible()
        self.go_to_element(element=moving_element)
        previous_position = self.get_element_position(element=moving_element)
        with allure.step("Move Container Restricted element"):
            try:
                self.action_drag_and_drop_by_offset(element=moving_element,
                                                    x_coards=random.randint(1, 600),
                                                    y_coards=random.randint(1, 200))
                result_position = self.get_element_position(element=moving_element)
            except TimeoutException:
                result_position = self.get_element_position(element=moving_element)
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
            if result_position[0]> 13 or result_position[1] > 86:
                return False
        return previous_position != result_position
