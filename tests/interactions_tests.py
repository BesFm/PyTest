import time

from conftest import driver
from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage


class TestInteractions:

    class TestSortable:

        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()
            unsorted_lists, sorted_lists = sortable_page.change_elements_positions()
            assert len(unsorted_lists[0]) == len(sorted_lists[0]) and unsorted_lists[0] != sorted_lists[0], \
                "Grid elements isn't replaced"
            assert len(unsorted_lists[1]) == len(sorted_lists[1]) and unsorted_lists[1] != sorted_lists[1], \
                "List elements isn't replaced"

    class TestSelectable:
        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable_page.open()
            list_elements, list_approved = selectable_page.select_elements("list")
            grid_elements, grid_approved = selectable_page.select_elements("grid")
            assert len(list_elements) == 3 and list_approved, "List elements isn't selected"
            assert len(grid_elements) == 3 and grid_approved, "Grid elements isn't selected"

    class TestResizablePage:

        def test_resizable_page(self, driver):
            resizable_page = ResizablePage(driver, "https://demoqa.com/resizable")
            resizable_page.open()
            resizable_page.remove_footer()
            box_sizes = resizable_page.resize_window("box window")
            simple_sizes = resizable_page.resize_window("simple window")
            assert box_sizes[0] != box_sizes[1] != box_sizes[2], "Box-window size isn't changed"
            assert box_sizes[1][0] <= 500 and box_sizes[1][1] <= 300, "Max size box-window exceeded"
            assert box_sizes[2][0] >= 150 and box_sizes[2][1] >= 150, "Min size box-window exceeded"
            assert simple_sizes[0] != simple_sizes[1] != simple_sizes[2], "Simple-window isn't changed"

    class TestDroppablePage:

        def test_simple_tab(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            simple_target_text = droppable_page.move_simple_box()
            assert simple_target_text == "Dropped!", "Element isn't moved to target or target hasn't react"

        def test_accept_tab(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            not_accept_text, accept_text = droppable_page.move_acceptable_box()
            assert not_accept_text == "Drop here", "Target react at wrong element or has been react before"
            assert accept_text == "Dropped!", "Element isn't moved to target or target hasn't react"

        def test_greedy_tab(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            greedy_page_result = droppable_page.move_greedy_box()
            assert greedy_page_result[0][0] == greedy_page_result[0][1], ("One of the target is greedy"
                                                                          " while it shouldn't be")
            assert greedy_page_result[1][0] != greedy_page_result[1][1], ("One of the target isn't greedy"
                                                                          " while it should be")
            assert greedy_page_result[2][0] == greedy_page_result[2][1], ("Element hasn't been moved to second target"
                                                                          "or target isn't react")

        def test_revert_tab(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            result_text, moving_assignment = droppable_page.move_revertable_box()
            assert result_text == "Dropped!", "Element isn't moved to target or target hasn't react"
            assert moving_assignment, "Element ISN'T MOVE back while it should or element MOVE back when it shouldn't"
