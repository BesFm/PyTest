from elements.base.base_element import BaseElement


class Title(BaseElement):
    def __init__(self, driver, locator):
        super().__init__(driver=driver, locator=locator)
