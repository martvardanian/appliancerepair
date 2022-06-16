import time

from Data.data_python import data
from Locators.locators import GenericLocators
from Pages.basepage import BasePage


class ContactPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver)
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(2)

    def fill_contact_form(self):
        self.send_keys(GenericLocators.first_name, data['fresno']['user']['firstname'])
        self.send_keys(GenericLocators.last_name, data['fresno']['user']['lastname'])
        self.send_keys(GenericLocators.email, data['fresno']['user']['email'])
        self.send_keys(GenericLocators.phone_number, data['fresno']['user']['phone_number'])
        self.send_keys(GenericLocators.message, data['fresno']['user']['message'])
        time.sleep(2)

    def send_contact(self):
        self.click_js(GenericLocators.send_button)
        time.sleep(1)
