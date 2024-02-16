from abc import ABC

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(ABC):
    """
    Базовая страница, предоставляющая все необходимые виды возможных элементов и действий с ними:
    ***Виды элементов***
    element_is_visible - возвращает оидн объект, если он в зоне видимости для пользователя(для selenium также)
    elements_are_visible - возвращает список объектов, если они в зоне видимости для пользователя(для selenium также)
    element_is_present - возвращает оидн объект, если он присутствует в дом-дереве тестируемой страницы
    elements_are_present - возвращает список объектов, если они присутствуют в дом-дереве тестируемой страницы
    element_is_not_visible - возвращает один объект, если он не виден для пользователя(для selenium также)
    element_is_clickable - возвращает один объект, если он кликабельный
    """

    wait_time = 5

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=wait_time):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=wait_time):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=wait_time):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=wait_time):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=wait_time):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=wait_time):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    """
    ***Действия с элеметнами***
    go_to_element - перемещает зону видимости на объект
    switch_to_tab - переключается на выбранную вкладку --> self.switch_to_tab(self.driver.window_handles[-1])
    action_double_click - производит двойное нажатие на объект
    action_right_click - производит нажатие ПКМ на объект
    action_move_to - устанавливает курсор на объект
    action_drag_and_drop_to - перемещает объект к выбранной цели(объекту)
    action_drag_and_drop_by_offset - перемещает объект на расстояние (x) по оси абсцисс и (y) по оси ординат
    remove_element - удаляет элемент из дом-дерева
    """

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def switch_to_tab(self, tab):
        self.driver.switch_to.window(tab)

    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    def action_move_to(self, element):
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
