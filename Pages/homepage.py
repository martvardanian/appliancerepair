import time

from Configs.configs import Urls
from Locators.locators import *
from Pages.basepage import BasePage


class HomePage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver)
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(2)

    def click_header_link(self, by_locator):
        self.click(by_locator)
        time.sleep(1)

    def click_footer_link(self, by_locator):
        self.click_js(by_locator)
        time.sleep(1)

    def click_popup_service(self, service_name_locator):
        self.click_header_link(GenericLocators.services_header)
        time.sleep(1)
        if Urls.Vegas in self.driver.current_url:
            self.click_header_link(GenericLocators.services_header_active)
        self.click(service_name_locator)
        time.sleep(1)

    def click_popup_service_active(self, service_name_locator):
        self.click_header_link(GenericLocators.services_header_active)
        time.sleep(1)
        self.click(service_name_locator)
        time.sleep(3)

    def click_read_more(self):
        self.click(FresnoLocators.read_more_index)
        time.sleep(1)


