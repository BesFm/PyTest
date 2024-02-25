import allure
from selenium.webdriver.chrome.webdriver import WebDriver

from conftest import driver
from pages_new.interactions_page_new import SortablePage, SelectablePage, ResizablePage, \
    DroppablePage, DraggablePage


@allure.suite("Test Interactions")
class TestInteractions:
    @allure.feature("Test Sortable")
    class TestSortable:
        @allure.title("Test sorting elements of list")
        def test_sortable_list(self, driver: WebDriver):
            sortable_page = SortablePage(driver=driver)
            sortable_page.open()
            assert sortable_page.check_elements_sorting("list"), \
                "List elements hasn't been sorted"

        @allure.title("Test sorting elements of grid")
        def test_sortable_grid(self, driver: WebDriver):
            sortable_page = SortablePage(driver=driver)
            sortable_page.open()
            assert sortable_page.check_elements_sorting("grid"), \
                "Grid elements hasn't been sorted"

    @allure.feature("Test Selectable")
    class TestSelectable:

        @allure.title("Test selectable list")
        def test_selectable_list(self, driver: WebDriver):
            selectable_page = SelectablePage(driver=driver)
            selectable_page.open()
            assert selectable_page.check_selected_elements("list"), \
                "Not all elements has been selected at list tab"

        @allure.step("Test selectable grid")
        def test_selectable_grid(self, driver: WebDriver):
            selectable_page = SelectablePage(driver=driver)
            selectable_page.open()
            assert selectable_page.check_selected_elements("grid"), \
                "Not all elements has been selected at grid tab"

    @allure.feature("Test Resizable")
    class TestResizable:

        @allure.title("Test Resizable box window")
        def test_resizable_box_window(self, driver: WebDriver):
            resizable_page = ResizablePage(driver=driver)
            resizable_page.open()
            assert resizable_page.check_resizing_of_box_window(), \
                "Box window size hasn't been changed"

        @allure.title("Test Resizable simple window")
        def test_resizable_simple_window(self, driver: WebDriver):
            resizable_page = ResizablePage(driver=driver)
            resizable_page.open()
            assert resizable_page.check_resizing_of_simple_window(), \
                "Simple window size hasn't been changed"

    @allure.feature("Test Droppable")
    class TestDroppable:

        @allure.title("Test simple target")
        def test_simple_target(self, driver: WebDriver):
            droppable_page = DroppablePage(driver=driver)
            droppable_page.open()
            assert droppable_page.move_simple_box_and_get_result() == "Dropped!", \
                "Element hasn't been moved to target or target doesn't react"

        @allure.title("Test acceptable target")
        def test_acceptable_target(self, driver: WebDriver):
            droppable_page = DroppablePage(driver=driver)
            droppable_page.open()
            assert droppable_page.move_not_acceptable_element_and_get_result() == "Drop here", \
                "Target react at wrong element or has been react before"
            assert droppable_page.move_acceptable_element_and_get_result() == "Dropped!", \
                "Element isn't moved to target or target hasn't react"

        @allure.title("Test greedy tab - Move element to not greedy target")
        def test_not_greedy_target(self, driver: WebDriver):
            droppable_page = DroppablePage(driver=driver)
            droppable_page.open()
            outer_result, inner_result = droppable_page.moving_element_to_not_greedy_target()
            assert outer_result == inner_result, \
                "Inner target is greedy when it shouldn't be"

        @allure.title("Test greedy tab - Move element to greedy target")
        def test_greedy_target(self, driver: WebDriver):
            droppable_page = DroppablePage(driver=driver)
            droppable_page.open()
            outer_result, inner_result = droppable_page.moving_element_to_greedy_target()
            assert outer_result != inner_result, \
                "Inner target isn't greedy when it should be"

        @allure.title("Test greedy tab - Move element to EACH greedy targets")
        def test_each_greedy_target(self, driver: WebDriver):
            droppable_page = DroppablePage(driver=driver)
            droppable_page.open()
            outer_result, inner_result = droppable_page.moving_element_to_each_greedy_targets()
            assert outer_result == inner_result, \
                "Element hasn't been moved to outer target, or outer target doesn't react"

        @allure.title("Test revertable element")
        def test_revertable_element(self, driver: WebDriver):
            droppable_page = DroppablePage(driver=driver)
            droppable_page.open()
            assert droppable_page.check_moving_of_revertable_element(), \
                "Revertable element doesn't revert when it should"

        @allure.title("Test non revertable element")
        def test_revertable_element(self, driver: WebDriver):
            droppable_page = DroppablePage(driver=driver)
            droppable_page.open()
            assert droppable_page.check_moving_of_non_revertable_element(), \
                "Non Revertable element is revert when it shouldn't"

    @allure.feature("Test Draggable")
    class TestDraggable:

        @allure.title("Test simple moving element")
        def test_simple_moving_box(self, driver: WebDriver):
            draggable_page = DraggablePage(driver=driver)
            draggable_page.open()
            assert draggable_page.check_moving_simple_element(), \
                "Simple moving element hasn't been moved"

        @allure.title("Test moving 'Y' axis restricted  element")
        def test_moving_axis_x_element(self, driver: WebDriver):
            draggable_page = DraggablePage(driver=driver)
            draggable_page.open()
            assert draggable_page.check_moving_axis_element(element="x_element"), \
                "Axis element has been moved by wrong axis or hasn't been moved"

        @allure.title("Test moving 'X' axis restricted  element")
        def test_moving_axis_y_element(self, driver: WebDriver):
            draggable_page = DraggablePage(driver=driver)
            draggable_page.open()
            assert draggable_page.check_moving_axis_element(element="y_element"), \
                "Axis element has been moved by wrong axis or hasn't been moved"

        @allure.title("Test moving 'BOX' restricted element")
        def test_moving_box_contained_element(self, driver: WebDriver):
            draggable_page = DraggablePage(driver=driver)
            draggable_page.open()
            assert draggable_page.check_moving_container_element(
                element="box_contained"), \
        "Box contained element has been moved out from box border or hasn't been moved"

        @allure.title("Test moving 'PARENT' restricted element")
        def test_moving_parent_contained_element(self, driver: WebDriver):
            draggable_page = DraggablePage(driver=driver)
            draggable_page.open()
            assert draggable_page.check_moving_container_element(
                element="parent_contained"), \
        "Parent contained element has been moved out from parent border or hasn't been moved"
