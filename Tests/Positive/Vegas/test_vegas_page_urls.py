import time
from Configs.configs import Urls
from Locators.locators import VegasLocators, GenericLocators
from Pages.basepage import BasePage
from Pages.homepage import HomePage
from Tests.basetest import BaseTest


class Test_pages(BaseTest):
    def test_check_header_footer_urls_and_titles(self, setup):
        try:
            self.driver = setup
            self.homePage = HomePage(self.driver, Urls.Vegas)
            self.basePage = BasePage(self.driver)

            """ Header """
            self.homePage.click_header_link(GenericLocators.service_areas_header)
            assert 'service-areas' in self.driver.current_url
            assert 'Service Areas' in self.basePage.get_text_from_index(VegasLocators.page_title, 1)

            self.homePage.click_header_link(GenericLocators.services_header)
            assert 'services' in self.driver.current_url
            assert 'Services' in self.basePage.get_text_from_index(VegasLocators.page_title, 1)

            self.homePage.click_header_link(GenericLocators.brands_header)
            assert 'brands' in self.driver.current_url
            assert 'Brands' in self.basePage.get_text_from_index(VegasLocators.page_title, 1)

            self.homePage.click_header_link(GenericLocators.contact_header)
            assert 'contact-us' in self.driver.current_url
            assert 'Contact Us' in self.basePage.get_text_from_index(VegasLocators.page_title, 1)

            self.homePage.click_header_link(VegasLocators.menu_logo)
            assert 'home' in self.driver.current_url
            assert 'Trusted Appliance Repair\nServices In Vegas' in self.basePage.get_text(VegasLocators.banner_title)

            self.homePage.click_header_link(GenericLocators.schedule_service_header)
            assert 'schedule-service' in self.driver.current_url
            assert 'Schedule Service' in self.basePage.get_text_from_index(VegasLocators.page_title, 1)

            """ Footer """
            self.homePage.click_footer_link(GenericLocators.service_areas_header)
            assert 'service-areas' in self.driver.current_url
            assert 'Service Areas' in self.basePage.get_text_from_index(VegasLocators.page_title, 1)

            self.homePage.click_footer_link(GenericLocators.brands_footer)
            assert 'brands' in self.driver.current_url
            assert 'Brands' in self.basePage.get_text_from_index(VegasLocators.page_title, 1)

            self.homePage.click_footer_link(GenericLocators.contact_footer)
            assert 'contact-us' in self.driver.current_url
            assert 'Contact Us' in self.basePage.get_text_from_index(VegasLocators.page_title, 1)

            self.homePage.click_footer_link(GenericLocators.services_footer)
            assert 'services' in self.driver.current_url
            assert 'Services' in self.basePage.get_text_from_index(VegasLocators.page_title, 1)
        finally:
            self.driver.close()

    def test_check_single_pages_urls_and_titles(self, setup):
        try:
            self.driver = setup
            self.homePage = HomePage(self.driver, Urls.Vegas)
            self.basePage = BasePage(self.driver)

            self.homePage.click_popup_service(GenericLocators.popup_refrigerator)
            assert 'refrigerator-repair' in self.driver.current_url
            assert 'Refrigerator Repair' in self.basePage.get_text(VegasLocators.service_title)

            self.homePage.click_popup_service_active(GenericLocators.popup_range)
            assert 'range-hood-repair' in self.driver.current_url
            assert 'Range Hood Repair' in self.basePage.get_text(VegasLocators.service_title)

            self.homePage.click_popup_service_active(GenericLocators.popup_dryer)
            assert 'dryer-repair' in self.driver.current_url
            assert 'Dryer Repair' in self.basePage.get_text(VegasLocators.service_title)

            self.homePage.click_popup_service_active(GenericLocators.popup_washer)
            assert 'washer-repair' in self.driver.current_url
            assert 'Washer Repair' in self.basePage.get_text(VegasLocators.service_title)

            self.homePage.click_popup_service_active(GenericLocators.popup_microwave)
            assert 'microwave-repair' in self.driver.current_url
            assert 'Microwave Repair' in self.basePage.get_text(VegasLocators.service_title)

            self.homePage.click_popup_service_active(GenericLocators.popup_oven)
            assert 'oven-repair' in self.driver.current_url
            assert 'Oven Repair' in self.basePage.get_text(VegasLocators.service_title)

            self.homePage.click_popup_service_active(GenericLocators.popup_freezer)
            assert 'freezer-repair' in self.driver.current_url
            assert 'Freezer Repair' in self.basePage.get_text(VegasLocators.service_title)

            self.homePage.click_popup_service_active(GenericLocators.popup_stove)
            assert 'stove-repair' in self.driver.current_url
            assert 'Stove Repair' in self.basePage.get_text(VegasLocators.service_title)

            self.homePage.click_popup_service_active(GenericLocators.popup_dishwasher)
            assert 'dishwasher-repair' in self.driver.current_url
            assert 'Dishwasher Repair' in self.basePage.get_text(VegasLocators.service_title)

            self.homePage.click_popup_service_active(GenericLocators.popup_wine)
            assert 'wine-cooler-repair' in self.driver.current_url
            assert 'Wine Cooler Repair' in self.basePage.get_text(VegasLocators.service_title)

            self.homePage.click_popup_service_active(GenericLocators.popup_trash)
            assert 'trash-compactor-repair' in self.driver.current_url
            assert 'Trash Compactor Repair' in self.basePage.get_text(VegasLocators.service_title)

            self.homePage.click_popup_service_active(GenericLocators.popup_garbage)
            assert 'garbage-disposal-repair' in self.driver.current_url
            assert 'Garbage Disposal Repair' in self.basePage.get_text(VegasLocators.service_title)
        finally:
            self.driver.close()

    def test_check_card_and_title(self, setup):
        try:
            self.driver = setup
            self.homePage = HomePage(self.driver, Urls.Vegas)
            self.basePage = BasePage(self.driver)

            cart_title = self.homePage.get_text(VegasLocators.cart_title)
            self.homePage.click_js(VegasLocators.cart_title)
            time.sleep(5)
            assert cart_title in self.basePage.get_text(VegasLocators.service_title)

        finally:
            self.driver.close()
