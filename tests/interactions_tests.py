from conftest import driver
from pages.interactions_page import SortablePage


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
