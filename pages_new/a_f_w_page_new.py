import time
import allure
from elements.buttons import Button
from elements.frame import Frame
from elements.title import Title
from generator.generator import generated_person
from locators.a_f_w_page_locators import (BrowserWindowsPageLocators, AlertsPageLocators,
                                          FramePageLocators, NestedFrameLocators,
                                          ModalPageLocators)
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, url="https://demoqa.com/browser-windows")

        self.new_tab_button = Button(driver=driver,
                                     locator=BrowserWindowsPageLocators.NEW_TAB_BUTTON)
        self.new_window_button = Button(driver=driver,
                                        locator=BrowserWindowsPageLocators.NEW_WINDOW_BUTTON)
        self.response_title = Title(driver=driver,
                                    locator=BrowserWindowsPageLocators.RESPONSE_TITLE)

    @allure.step("Open New Tab or New Window Button")
    def check_tab_or_window_button(self, button: str) -> bool:
        dictic = {"new_tab": self.new_tab_button.is_visible(),
                  "new_window": self.new_window_button.is_visible()}
        dictic[button].click()
        self.switch_to_tab(self.driver.window_handles[-1])
        response_title = self.response_title.is_visible().text
        return response_title == "This is a sample page"


class AlertsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, url="https://demoqa.com/alerts")

        self.simple_alert_button = Button(driver=driver,
                                          locator=AlertsPageLocators.SIMPLE_ALERT_BUTTON)
        self.time_alert_button = Button(driver=driver,
                                        locator=AlertsPageLocators.TIME_ALERT_BUTTON)
        self.confirm_alert_button = Button(driver=driver,
                                           locator=AlertsPageLocators.CONFIRM_ALERT_BUTTON)
        self.confirm_alert_title = Title(driver=driver,
                                         locator=AlertsPageLocators.CONFIRM_RESULT)
        self.prompt_alert_button = Button(driver=driver,
                                          locator=AlertsPageLocators.PROMPT_ALERT_BUTTON)
        self.prompt_alert_title = Title(driver=driver,
                                        locator=AlertsPageLocators.PROMPT_RESULT)

    @allure.step("Call simple or time alert")
    def check_simple_or_time_alert(self, button: str) -> bool:
        dictic = {"simple": [self.simple_alert_button.is_visible(), 0],
                  "time": [self.time_alert_button.is_visible(), 5]}
        dictic[button][0].click()
        time.sleep(dictic[button][1])
        alert_window = self.driver.switch_to.alert
        result_dictic = {"simple": "You clicked a button",
                         "time": "This alert appeared after 5 seconds"}
        return alert_window.text == result_dictic[button]

    @allure.step("Call Confirm alert")
    def check_confirm_alert(self, choice: str) -> bool:
        self.confirm_alert_button.is_visible().click()
        alert_window = self.driver.switch_to.alert
        with allure.step("Confirm or dismiss alert"):
            if choice == "accept":
                alert_window.accept()
            elif choice == "dismiss":
                alert_window.dismiss()
            dictic = {"accept": "You selected Ok", "dismiss": "You selected Cancel"}
        return dictic[choice] == self.confirm_alert_title.is_visible().text

    @allure.step("Call Prompt alert")
    def check_prompt_alert(self) -> bool:
        fullname = next(generated_person()).full_name
        self.prompt_alert_button.is_visible().click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(fullname)
        alert_window.accept()
        return fullname == self.prompt_alert_title.is_visible().text.strip("You entered ")


class FramesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, url="https://demoqa.com/frames")

        self.big_frame = Frame(driver=driver, locator=FramePageLocators.FIRST_FRAME)
        self.little_frame = Frame(driver=driver, locator=FramePageLocators.SECOND_FRAME)
        self.frame_content = Title(driver=driver, locator=FramePageLocators.RESPONSE_FRAME)

    @allure.step("Read Frame content")
    def get_frame_content(self, frame_num: str) -> tuple[str, str, str]:
        dictic = {"frame1": self.big_frame.is_visible(),
                  "frame2": self.little_frame.is_visible()}
        width = dictic[frame_num].get_attribute("width")
        height = dictic[frame_num].get_attribute("height")
        self.driver.switch_to.frame(dictic[frame_num])
        frame_content = self.frame_content.is_visible().text
        self.driver.switch_to.default_content()
        return width, height, frame_content


class NestedFramesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, url="https://demoqa.com/nestedframes")

        self.large_nested_frame = Frame(driver=driver,
                                        locator=NestedFrameLocators.LARGE_FRAME)
        self.large_nested_frame_content = Title(driver=driver,
                                                locator=NestedFrameLocators.LFRAME_TEXT)
        self.small_nested_frame = Frame(driver=driver,
                                        locator=NestedFrameLocators.SMALL_FRAME)
        self.small_nested_frame_content = Title(driver=driver,
                                                locator=NestedFrameLocators.SFRAME_TEXT)

    @allure.step("Read Nested Frames content")
    def get_nested_frame_content(self) -> tuple[str, str]:
        self.driver.switch_to.frame(self.large_nested_frame.is_visible())
        large_frame_text = self.large_nested_frame_content.is_visible().text
        self.driver.switch_to.frame(self.small_nested_frame.is_visible())
        small_frame_text = self.small_nested_frame_content.is_visible().text
        return large_frame_text, small_frame_text


class ModalDialogsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, url="https://demoqa.com/modal-dialogs")

        self.open_small_modal = Button(driver=driver,
                                       locator=ModalPageLocators.OPEN_SMALL_MODAL)
        self.close_small_modal = Button(driver=driver,
                                        locator=ModalPageLocators.CLOSE_SMALL_MODAL)
        self.open_large_modal = Button(driver=driver,
                                       locator=ModalPageLocators.OPEN_LARGE_MODAL)
        self.close_large_modal = Button(driver=driver,
                                        locator=ModalPageLocators.CLOSE_LARGE_MODAL)
        self.modal_header = Title(driver=driver,
                                  locator=ModalPageLocators.MODAL_HEADER)

    @allure.step("Open Small Modal")
    def get_small_modal_content(self) -> str:
        self.open_small_modal.is_visible().click()
        small_modal_header = self.modal_header.is_visible().text
        self.close_small_modal.is_visible().click()
        time.sleep(0.5)
        return small_modal_header

    @allure.step("Open Large Modal")
    def get_large_modal_content(self) -> str:
        self.open_large_modal.is_visible().click()
        large_modal_header = self.modal_header.is_visible().text
        self.close_large_modal.is_visible().click()
        time.sleep(0.5)
        return large_modal_header
