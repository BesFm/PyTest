from abc import ABC

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement(ABC):
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
    time_out = 5

    def is_visible(self, set_timeout=time_out):
        return wait(driver=self.driver, timeout=set_timeout).until(
            EC.visibility_of_element_located(self.locator))

    def are_visible(self, set_timeout=time_out):
        return wait(driver=self.driver, timeout=set_timeout).until(
            EC.visibility_of_all_elements_located(self.locator))

    def is_present(self, set_timeout=time_out):
        return wait(driver=self.driver, timeout=set_timeout).until(
            EC.presence_of_element_located(self.locator))

    def are_present(self, set_timeout=time_out):
        return wait(driver=self.driver, timeout=set_timeout).until(
            EC.presence_of_all_elements_located(self.locator))

    def not_visible(self, set_timeout=time_out):
        return wait(driver=self.driver, timeout=set_timeout).until(
            EC.invisibility_of_element_located(self.locator))

    def is_clickable(self, set_timeout=time_out):
        return wait(driver=self.driver, timeout=set_timeout).until(
            EC.element_to_be_clickable(self.locator))

    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    def action_hover(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    def action_drag_and_drop_to(self, source, target):
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target)
        action.perform()

    def action_drag_and_drop_by_offset(self, element, x_coards, y_coards):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_coards, y_coards)
        action.perform()

    def remove_element(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        self.driver.execute_script(" document.getElementById('fixedban').remove();")
