import random
import time

import allure

from pages.base_page import BasePage
from locators.a_f_w_page_locators import (BrowserWindowsPageLocators, AlertsPageLocators, FramePageLocators,
                                          NestedFramesLocators, ModalPageLocators)
from generator.generator import generated_person


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    @allure.step("Open New Tab or New Window Button")
    def open_tab_or_window(self, button):
        dictic = {"new_tab": self.locators.NEW_TAB_BUTTON, "new_window": self.locators.NEW_WINDOW_BUTTON}
        self.element_is_visible(dictic[button]).click()
        self.switch_to_tab(self.driver.window_handles[-1])
        response_title = self.element_is_visible(self.locators.RESPONSE_TITLE).text
        return response_title


class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    @allure.step("Call simple or time alert")
    def call_simple_time_alert(self, button):
        dictic = {"simple": [self.locators.SIMPLE_ALERT_BUTTON, 0], "time": [self.locators.TIME_ALERT_BUTTON, 5]}
        self.element_is_visible(dictic[button][0]).click()
        time.sleep(dictic[button][1])
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    @allure.step("Call Confirm alert")
    def call_confirm_alert(self):
        self.element_is_visible(self.locators.CONFIRM_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        var = ["accept", "dismiss"]
        with allure.step("Confirm or dismiss alert"):
            choice = random.choice(var)
            if choice == "accept":
                alert_window.accept()
            elif choice == "dismiss":
                alert_window.dismiss()
            dictic = {var[0]: "You selected Ok", var[1]: "You selected Cancel"}
        return dictic[choice], self.element_is_visible(self.locators.CONFIRM_RESULT).text

    @allure.step("Call Prompt alert")
    def call_prompt_alert(self):
        fullname = next(generated_person()).full_name
        self.element_is_visible(self.locators.PROMPT_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(fullname)
        alert_window.accept()
        return fullname, self.element_is_visible(self.locators.PROMPT_RESULT).text.lstrip("You entered ")


class FramesPage(BasePage):
    locators = FramePageLocators()

    @allure.step("Read Frame content")
    def get_frame_content(self, frame_num):
        dictic = {"frame1": self.locators.FIRST_FRAME, "frame2": self.locators.SECOND_FRAME}
        frame = self.element_is_visible(dictic[frame_num])
        width = frame.get_attribute("width")
        height = frame.get_attribute("height")
        self.driver.switch_to.frame(frame)
        frame_text = self.element_is_visible(self.locators.RESPONSE_FRAME).text
        self.driver.switch_to.default_content()
        return width, height, frame_text


class NestedFramesPage(BasePage):
    locators = NestedFramesLocators()

    @allure.step("Read Nested Frames content")
    def get_nested_frames_content(self):
        lframe = self.element_is_visible(self.locators.LARGE_FRAME)
        self.driver.switch_to.frame(lframe)
        lframe_text = self.element_is_visible(self.locators.LFRAME_TEXT).text
        sframe = self.element_is_visible(self.locators.SMALL_FRAME)
        self.driver.switch_to.frame(sframe)
        sframe_text = self.element_is_present(self.locators.SFRAME_TEXT).text
        return lframe_text, sframe_text


class ModalDialogsPage(BasePage):
    locators = ModalPageLocators()

    @allure.step("Open Small Modal")
    def call_small_modal(self):
        self.element_is_visible(self.locators.OPEN_SMALL_MODAL).click()
        small_modal_header = self.element_is_visible(self.locators.MODAL_HEADER).text
        self.element_is_visible(self.locators.CLOSE_SMALL_MODAL).click()
        return small_modal_header

    @allure.step("Open Large Modal")
    def call_large_modal(self):
        self.element_is_visible(self.locators.OPEN_LARGE_MODAL).click()
        large_modal_header = self.element_is_visible(self.locators.MODAL_HEADER).text
        self.element_is_visible(self.locators.CLOSE_LARGE_MODAL).click()
        return large_modal_header
