from elements.base.base_element import BaseElement


class Button(BaseElement):
    def __init__(self, driver, locator):
        super().__init__(driver=driver, locator=locator)
