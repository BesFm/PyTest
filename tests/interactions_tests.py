import allure

from conftest import driver
from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, \
    DroppablePage, DraggablePage


@allure.suite("Test Interactions")
class TestInteractions:
    @allure.feature("Test Sortable")
    class TestSortable:

        @allure.title("Check sorted elements of list")
        def test_sortable_list(self, driver):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()
            assert sortable_page.check_elements_sorting(
                "list"), "List elements hasn't been sorted"

        @allure.title("Check sorted elements of grid")
        def test_sortable_grid(self, driver):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()
            assert sortable_page.check_elements_sorting(
                "grid"), "Grid element's hasn't been sorted"

    @allure.feature("Test Selectable")
    class TestSelectable:

        @allure.title("Check Sorted elements of list")
        def test_selectable_list(self, driver):
            selectable_page = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable_page.open()
            assert selectable_page.check_selected_elements(
                "list"), "List elements hasn't been selected"

        @allure.title("Check Sorted elements of grid")
        def test_selectable_grid(self, driver):
            selectable_page = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable_page.open()
            assert selectable_page.check_selected_elements(
                "grid"), "Grid elements isn't selected"

    @allure.feature("Test Resizable")
    class TestResizable:

        @allure.title("Check resized box window")
        def test_resizable_box(self, driver):
            resizable_page = ResizablePage(driver, "https://demoqa.com/resizable")
            resizable_page.open()
            test_result, message = resizable_page.check_resizing_of_box_window()
            assert test_result, message

        @allure.title("Check resized simple window")
        def test_resizable_simple(self, driver):
            resizable_page = ResizablePage(driver, "https://demoqa.com/resizable")
            resizable_page.open()
            assert resizable_page.check_resizing_of_simple_window(), "Simple-window isn't changed"

    @allure.feature("Test Droppable")
    class TestDroppable:

        @allure.title("Test element at simple tab")
        def test_simple_tab(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            assert droppable_page.move_simple_box == "Dropped!", "Element isn't moved to target or target hasn't react"

        @allure.title("Test element at accept tab")
        def test_accept_tab(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            not_accept_text, accept_text = droppable_page.move_acceptable_box()
            assert not_accept_text == "Drop here", "Target react at wrong element or has been react before"
            assert accept_text == "Dropped!", "Element isn't moved to target or target hasn't react"

        @allure.title("Test element at prevent propagation tab - Not Greedy container")
        def test_not_greedy_tab(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            outer_container, inner_container = droppable_page.move_box_to_not_greedy_container()
            assert outer_container == inner_container, "One of the target is greedy while it shouldn't be"

        @allure.title("Test element at prevent propagation tab - Not Greedy container")
        def test_greedy_tab(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            test_result, message = droppable_page.check_moving_to_greedy_container()
            assert test_result, message  # в модуле page генерируется сообщение ошибки в зависимости от ошибки

        @allure.title("Test element at revert draggable tab")
        def test_revert_tab(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            result_text, moving_assignment = droppable_page.move_revertable_box(
                move_type="will revert")
            assert result_text == "Dropped!", "Element isn't moved to target or target hasn't react"
            assert moving_assignment, "Element ISN'T MOVE back while it should or element MOVE back when it shouldn't"

        @allure.title("Test element at revert draggable tab")
        def test_revert_tab(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            result_text, moving_assignment = droppable_page.move_revertable_box(
                move_type="not revert")
            assert result_text == "Dropped!", "Element isn't moved to target or target hasn't react"
            assert moving_assignment, "Element ISN'T MOVE back while it should or element MOVE back when it shouldn't"

    @allure.feature("Test Draggable")
    class TestDraggable:

        @allure.title("Test element at Simple tab")
        def test_simple_tab(self, driver):
            draggable_page = DraggablePage(driver, "https://demoqa.com/dragabble")
            draggable_page.open()
            assert draggable_page.check_moving_simple_element(), "Element hasn't been moved"

        @allure.title("Test element at Axis Restricted tab")
        def test_axis_restricted_tab(self, driver):
            draggable_page = DraggablePage(driver, "https://demoqa.com/dragabble")
            draggable_page.open()
            assert draggable_page.check_moving_axis_element(
                "y_element"), "'Y' element hasn't been moved or made x move"
            assert draggable_page.check_moving_axis_element(
                "x_element"), "'X' element hasn't been moved or made y move"

        @allure.title("Test element at Container Restricted tab")
        def test_container_restricted_tab(self, driver):
            draggable_page = DraggablePage(driver, "https://demoqa.com/dragabble")
            draggable_page.open()
            assert draggable_page.check_moving_container_element("box_contained"), \
                "Box contained element hasn't been moved or moved over the box border"
            assert draggable_page.check_moving_container_element("parent_contained"), \
                "Parent contained element hasn't been moved or moved over the parent border"
