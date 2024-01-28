from conftest import driver
from pages.a_f_w_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage


class TestAlertsFrameWindows:

    class TestBrowserWindows:
        def test_new_tab(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_windows_page.open()
            new_tab_title = browser_windows_page.check_button("new_tab")
            assert new_tab_title == "This is a sample page", "Tab isn't opened"

        def test_new_window(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_windows_page.open()
            new_window_title = browser_windows_page.check_button("new_window")
            assert new_window_title == "This is a sample page", "Tab isn't opened"

    class TestAlerts:

        def test_simple_alert_button(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()
            alert_text = alerts_page.check_alert_buttons("simple")
            assert alert_text == "You clicked a button", "Alert isn't appear"

        def test_time_alert_button(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()
            alert_text = alerts_page.check_alert_buttons("time")
            assert alert_text == "This alert appeared after 5 seconds", "Alert isn't appear"

        def test_confirm_alert_button(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()
            exp, fact = alerts_page.check_confirm_alert()
            assert exp == fact, "Something wrong with alert"

        def test_prompt_alert_button(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()
            exp, fact = alerts_page.check_prompt_alert()
            assert exp == fact, "Something wrong with alert"

    class TestFrames:

        def test_frames(self, driver):
            frames_page = FramesPage(driver, "https://demoqa.com/frames")
            frames_page.open()
            fwidth1, fheight1, ftext1 = frames_page.check_frame("frame1")
            fwidth2, fheight2, ftext2 = frames_page.check_frame("frame2")
            assert fwidth1 != fwidth2, "Frame's width's equal or it's same frame"
            assert fheight1 != fheight2, "Frame's height's equal or it's same frame"
            assert ftext1 == "This is a sample page", "Frame's content differs from expected"
            assert ftext2 == "This is a sample page", "Frame's content differs from expected"

    class TestNestedFrames:

        def test_nested_frames(self, driver):
            nestframes_page = NestedFramesPage(driver, "https://demoqa.com/nestedframes")
            nestframes_page.open()
            lframe_text, sframe_text = nestframes_page.check_nested_frames()
            assert lframe_text == "Parent frame", "Frame's content differs from expected"
            assert sframe_text == "Child Iframe", "Frame's content differs from expected"
