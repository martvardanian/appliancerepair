import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Data.data_python import data
from Locators.locators import GenericLocators
from Pages.basepage import BasePage


class SchedulePage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver)
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(2)

    def fill_schedule_form(self):
        self.send_keys(GenericLocators.first_name, data['fresno']['user']['firstname'])
        self.send_keys(GenericLocators.last_name, data['fresno']['user']['lastname'])
        self.send_keys(GenericLocators.email, data['fresno']['user']['email'])
        self.send_keys(GenericLocators.phone_number, data['fresno']['user']['phone_number'])
        # City
        self.click_js(GenericLocators.city)
        select = Select(self.driver.find_element(By.NAME, 'city'))
        select.select_by_index(6)
        self.send_keys(GenericLocators.address, data['fresno']['user']['address'])
        self.send_keys(GenericLocators.zip, data['fresno']['user']['zip'])
        # Appliance
        self.click_js(GenericLocators.appliance)
        select = Select(self.driver.find_element(By.NAME, 'appliance'))
        select.select_by_index(6)
        # Brand
        self.click_js(GenericLocators.brand)
        select = Select(self.driver.find_element(By.NAME, 'brand'))
        select.select_by_index(6)
        self.send_keys(GenericLocators.service_date, data['fresno']['user']['date'])
        self.send_keys(GenericLocators.service_time, data['fresno']['user']['time'] + data['fresno']['user']['am'])
        self.send_keys(GenericLocators.message, data['fresno']['user']['message'])
        time.sleep(2)

    def click_schedule_service(self):
        self.click_js(GenericLocators.schedule_service_button)
        time.sleep(1)
