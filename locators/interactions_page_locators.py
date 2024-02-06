from selenium.webdriver.common.by import By


class SortablePageLocators:

    GRID_TAB = (By.CSS_SELECTOR, "a[id='demo-tab-grid']")
    GRID_ELEMENTS = (By.CSS_SELECTOR, "div[class='create-grid'] div")
    LIST_TAB = (By.CSS_SELECTOR, "a[id='demo-tab-list']")
    LIST_ELEMENTS = (By.CSS_SELECTOR, "div[class='vertical-list-container mt-4'] div")


class SelectablePageLocators:

    LIST_TAB = (By.CSS_SELECTOR, "a[id='demo-tab-list']")
    LIST_ELEMENTS = (By.CSS_SELECTOR, "li[class='mt-2 list-group-item list-group-item-action']")
    GRID_TAB = (By.CSS_SELECTOR, "a[id='demo-tab-grid']")
    GRID_ELEMENTS = (By.CSS_SELECTOR, "li[class='list-group-item list-group-item-action']")


class ResizablePageLocators:

    RESIZABLE_BOX_WINDOW = (By.CSS_SELECTOR, "div[id='resizableBoxWithRestriction']")
    RESIZABLE_BOX_ARROW = (By.CSS_SELECTOR, "div[id='resizableBoxWithRestriction'] span")
    RESIZABLE_WINDOW = (By.CSS_SELECTOR, "div[id='resizable']")
    RESIZABLE_ARROW = (By.CSS_SELECTOR, "div[id='resizable'] span")


class DroppablePageLocators:

    # Simple Page
    SIMPLE_TAB = (By.CSS_SELECTOR, "a[id='droppableExample-tab-simple']")
    SIMPLE_MOVING_BOX = (By.CSS_SELECTOR, "div[id='draggable']")
    SIMPLE_TARGET_BOX = (By.CSS_SELECTOR, "div[id='simpleDropContainer'] div[id='droppable']")

    # Accept Page
    ACCEPTABLE_TAB = (By.CSS_SELECTOR, "a[id='droppableExample-tab-accept']")
    ACCEPTABLE_MOVING_BOX = (By.CSS_SELECTOR, "div[id='acceptable']")
    NOTACCEPTABLE_MOVING_BOX = (By.CSS_SELECTOR, "div[id='notAcceptable']")
    ACCEPT_TARGET_BOX = (By.CSS_SELECTOR, "div[id='acceptDropContainer'] div[id='droppable']")

    # Greedy Page
    GREEDY_TAB = (By.CSS_SELECTOR, "a[id='droppableExample-tab-preventPropogation']")
    GREEDY_MOVING_BOX = (By.CSS_SELECTOR, "div[id='dragBox']")
    INNER_NOTGREEDY_TARGET = (By.CSS_SELECTOR, "div[id='notGreedyInnerDropBox']")
    OUTER_NOTGREEDY_TARGET = (By.CSS_SELECTOR, "div[id='notGreedyDropBox']")
    INNER_GREEDY_TARGET = (By.CSS_SELECTOR, "div[id='greedyDropBoxInner']")
    OUTER_GREEDY_TARGET = (By.CSS_SELECTOR, "div[id='greedyDropBox']")

    # Revert Page
    REVERT_TAB = (By.CSS_SELECTOR, "a[id='droppableExample-tab-revertable']")
    REVERTABLE_MOVING_BOX = (By.CSS_SELECTOR, "div[id='revertable']")
    NONREVERTABLE_MOVING_BOX = (By.CSS_SELECTOR, "div[id='notRevertable']")
    REVERTABLE_TARGET_BOX = (By.CSS_SELECTOR, "div[id='revertableDropContainer'] div[id='droppable']")


class DraggablePageLocators:

    # Simple Tab
    SIMPLE_TAB = (By.CSS_SELECTOR, "a[id='draggableExample-tab-simple']")
    SIMPLE_MOVING_ELEMENT = (By.CSS_SELECTOR, "div[id='dragBox']")

    # Axis Restricted Tab
    AXIS_RESTRICTED_TAB = (By.CSS_SELECTOR, "a[id='draggableExample-tab-axisRestriction']")
    X_MOVING_ELEMENT = (By.CSS_SELECTOR, "div[id='restrictedX']")
    Y_MOVING_ELEMENT = (By.CSS_SELECTOR, "div[id='restrictedY']")

    # Container Restricted Tab
    CONTAINER_RESTRICTED_TAB = (By.CSS_SELECTOR, "a[id='draggableExample-tab-containerRestriction']")
    BOX_MOVING_TEXT = (By.CSS_SELECTOR, "div[class='draggable ui-widget-content ui-draggable ui-draggable-handle']")
    PARENT_MOVING_TEXT = (By.CSS_SELECTOR, "span[class='ui-widget-header ui-draggable ui-draggable-handle']")
