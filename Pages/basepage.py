"""This class is the parent of all pages"""
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""It contains all the generic methods and utilities for all the pages"""


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        self.driver.find_element(By.XPATH, by_locator)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, by_locator))).click()
        time.sleep(2)

    def get_text(self, by_locator):
        time.sleep(1)
        text = self.driver.find_element(By.XPATH, by_locator).text
        return text

    def get_text_from_index(self, by_locator, index):
        time.sleep(1)
        text = self.driver.find_elements(By.XPATH, by_locator)[index].text
        return text

    def click_js(self, by_locator):
        button = self.driver.find_element(By.XPATH, by_locator)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", button)

    def send_keys(self, by_locator, text):
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, by_locator))).send_keys(text)

    # def scroll_down(self):
    #     html = self.driver.find_element(By.TAG_NAME, 'html')
    #     html.send_keys(Keys.PAGE_DOWN)

    # def do_find_element_send_keys(self, by_selector, text):
    #     self.driver.find_element(by_selector).send_keys(text)
    #
    # def get_element_text(self, by_locator):
    #     element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
    #     return element.text
    #
    # def get_attribute_value(self, by_locator):
    #     element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
    #     return element.get_attribute('value')
    #
    # def is_visible(self, by_locator):
    #     element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
    #     return bool(element)
    #
    # def get_url(self, url):
    #     WebDriverWait(self.driver, 10).until(EC.url_to_be(url))
    #     return self.driver.current_url
    #
    # def select_checkboxes(self, from_num, to_num, by_selector):
    #     for i in range(from_num, to_num):
    #         self.driver.execute_script("arguments[0].click();", (self.driver.find_element((By.ID, by_selector % i))))
    #
    # def select_picture(self, by_locator, picture_path):
    #     self.driver.find_element(by_locator).send_keys(picture_path)
    #
    # def crop_picture(self, by_selected_picture):
    #     items = self.driver.find_element(By.XPATH, by_selected_picture)
    #     actions = ActionChains(self.driver)
    #     actions.drag_and_drop_by_offset(items, 500, 0).perform()
    #
    # def select_drop_down(self, index, by_locator):
    #     select = Select(self.driver.find_element(by_locator))
    #     select.select_by_index(index)




