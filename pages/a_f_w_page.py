import random
import time

from pages.base_page import BasePage
from locators.a_f_w_page_locators import BrowserWindowsPageLocators, AlertsPageLocators, FramePageLocators
from generator.generator import generated_person


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def check_button(self, button):
        dictic = {"new_tab": self.locators.NEW_TAB_BUTTON, "new_window": self.locators.NEW_WINDOW_BUTTON}
        self.element_is_visible(dictic[button]).click()
        self.switch_to_tab(self.driver.window_handles[-1])
        response_title = self.element_is_visible(self.locators.RESPONSE_TITLE).text
        return response_title


class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    def check_alert_buttons(self, button):
        dictic = {"simple": [self.locators.SIMPLE_ALERT_BUTTON, 0], "time": [self.locators.TIME_ALERT_BUTTON, 5]}
        self.element_is_visible(dictic[button][0]).click()
        time.sleep(dictic[button][1])
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_confirm_alert(self):
        self.element_is_visible(self.locators.CONFIRM_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        var = ["accept", "dismiss"]
        choice = random.choice(var)
        if choice == "accept":
            alert_window.accept()
        elif choice == "dismiss":
            alert_window.dismiss()
        dictic = {var[0]: "You selected Ok", var[1]: "You selected Cancel"}
        return dictic[choice], self.element_is_visible(self.locators.CONFIRM_RESULT).text

    def check_prompt_alert(self):
        fullname = next(generated_person()).full_name
        self.element_is_visible(self.locators.PROMPT_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(fullname)
        alert_window.accept()
        return fullname, self.element_is_visible(self.locators.PROMPT_RESULT).text.lstrip("You entered ")


class FramesPage(BasePage):
    locators = FramePageLocators()

    def check_frame(self, frame_num):
        dictic = {"frame1": self.locators.FIRST_FRAME, "frame2": self.locators.SECOND_FRAME}
        frame = self.element_is_visible(dictic[frame_num])
        width = frame.get_attribute("width")
        height = frame.get_attribute("height")
        self.driver.switch_to.frame(frame)
        frame_text = self.element_is_visible(self.locators.RESPONSE_FRAME).text
        self.driver.switch_to.default_content()
        return width, height, frame_text
