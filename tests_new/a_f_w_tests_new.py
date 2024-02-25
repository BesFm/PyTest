import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from conftest import driver
from pages_new.a_f_w_page_new import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage, ModalDialogsPage


@allure.suite("Test Alerts, Frame and Windows")
class TestAlertsFrameWindows:
    @allure.feature("Test Browser Windows")
    class TestBrowserWindows:
        @allure.title("Test New Tab button")
        def test_new_tab(self, driver: WebDriver):
            browser_windows_page = BrowserWindowsPage(driver=driver)
            browser_windows_page.open()
            assert browser_windows_page.check_tab_or_window_button(button="new_tab"), \
                "Tab isn't opened or content difference from expected"

        @allure.title("Test New Window Button")
        def test_new_window(self, driver: WebDriver):
            browser_windows_page = BrowserWindowsPage(driver=driver)
            browser_windows_page.open()
            assert browser_windows_page.check_tab_or_window_button(button="new_window"), \
                "Tab isn't opened or content difference from expected"

    @allure.feature("Test Alerts")
    class TestAlerts:

        @allure.title("Test Simple alert")
        def test_simple_alert(self, driver: WebDriver):
            alerts_page = AlertsPage(driver=driver)
            alerts_page.open()
            assert alerts_page.check_simple_or_time_alert(button="simple"), \
                "Alert isn't appear or alert's content different from expected"

        @allure.title("Test Time alert")
        def test_time_alert(self, driver: WebDriver):
            alerts_page = AlertsPage(driver=driver)
            alerts_page.open()
            assert alerts_page.check_simple_or_time_alert(button="time"), \
                "Alert isn't appear or alert's content different from expected"

        @allure.title("Test Confirm alert (accept)")
        def test_confirm_alert_accept(self, driver: WebDriver):
            alerts_page = AlertsPage(driver=driver)
            alerts_page.open()
            assert alerts_page.check_confirm_alert(choice="accept"), "Actual alert result difference from Expected"

        @allure.title("Test Confirm alert (dismiss)")
        def test_confirm_alert_dismiss(self, driver: WebDriver):
            alerts_page = AlertsPage(driver=driver)
            alerts_page.open()
            assert alerts_page.check_confirm_alert(choice="dismiss"), "Actual alert result difference from Expected"

        @allure.title("Test Prompt alert")
        def test_prompt_alert(self, driver: WebDriver):
            alerts_page = AlertsPage(driver=driver)
            alerts_page.open()
            assert alerts_page.check_prompt_alert(), "Alert's output difference from expected"

    @allure.feature("Test Frames")
    class TestFrames:

        @allure.title("Check Frames content")
        def test_frames(self, driver: WebDriver):
            frames_page = FramesPage(driver=driver)
            frames_page.open()
            width_frame1, height_frame1, text_frame1 = frames_page.get_frame_content("frame1")
            width_frame2, height_frame2, text_frame2 = frames_page.get_frame_content("frame2")
            assert width_frame1 != width_frame2, "Frame's width's equal or it's same frame"
            assert height_frame1 != height_frame2, "Frame's height's equal or it's same frame"
            assert text_frame1 == text_frame2 == "This is a sample page", "Frame's content differs from expected"

    @allure.feature("Test Nested Frames")
    class TestNestedFrames:

        @allure.title("Check Nested Frames content")
        def test_nested_frames(self, driver: WebDriver):
            nested_frames_page = NestedFramesPage(driver=driver)
            nested_frames_page.open()
            parent_frame_text, child_frame_text = nested_frames_page.get_nested_frame_content()
            assert parent_frame_text == "Parent frame", "Frame's content differs from expected"
            assert child_frame_text == "Child Iframe", "Frame's content differs from expected"

    @allure.feature("Test Modal Dialogs")
    class TestModalDialogs:

        @allure.title("Check Modal Dialogs content")
        def test_modal_dialogs(self, driver: WebDriver):
            modal_dialogs_page = ModalDialogsPage(driver=driver)
            modal_dialogs_page.open()
            assert modal_dialogs_page.get_small_modal_content() == "Small Modal", "Modal's content difference from expected"
            assert modal_dialogs_page.get_large_modal_content() == "Large Modal", "Modal's content difference from expected"
