from Configs.configs import Urls
from Locators.locators import FresnoLocators, GenericLocators
from Pages.basepage import BasePage
from Pages.homepage import HomePage
from Tests.basetest import BaseTest


class Test_pages(BaseTest):
    def test_check_header_footer_urls_and_titles(self, setup):
        try:
            self.driver = setup
            self.homePage = HomePage(self.driver, Urls.Fresno)
            self.basePage = BasePage(self.driver)

            """ Header """
            self.homePage.click_header_link(GenericLocators.about_header)
            assert 'about-us' in self.driver.current_url
            assert 'About Us' in self.basePage.get_text(FresnoLocators.page_title)

            # services page will be added
            # self.homePage.click_header_link(FresnoLocators.services_header)
            # assert 'services' in self.driver.current_url
            # assert 'Services' in self.basePage.get_text(self, FresnoLocators.page_title)

            self.homePage.click_header_link(GenericLocators.brands_header)
            assert 'brands' in self.driver.current_url
            assert 'Brands' in self.basePage.get_text(FresnoLocators.page_title)

            self.homePage.click_header_link(GenericLocators.contact_header)
            assert 'contact-us' in self.driver.current_url
            assert 'Contact Us' in self.basePage.get_text(FresnoLocators.page_title)

            self.homePage.click_header_link(GenericLocators.menu_logo)
            assert 'home' in self.driver.current_url
            assert 'Same Day Appliance Repair Services In Fresno, Clovis, Madera, Sanger, Friant And More' \
                   in self.basePage.get_text(FresnoLocators.banner_title)

            self.homePage.click_header_link(GenericLocators.schedule_service_header)
            assert 'schedule-service' in self.driver.current_url
            assert 'Schedule Service' in self.basePage.get_text(FresnoLocators.page_title)

            """ Footer """
            self.homePage.click_footer_link(GenericLocators.about_footer)
            assert 'about-us' in self.driver.current_url
            assert 'About Us' in self.basePage.get_text(FresnoLocators.page_title)

            self.homePage.click_footer_link(GenericLocators.brands_footer)
            assert 'brands' in self.driver.current_url
            assert 'Brands' in self.basePage.get_text(FresnoLocators.page_title)

            self.homePage.click_footer_link(GenericLocators.contact_footer)
            assert 'contact-us' in self.driver.current_url
            assert 'Contact Us' in self.basePage.get_text(FresnoLocators.page_title)

            # services page will be added
            # self.homePage.click_services_header()
            # assert 'services' in self.driver.current_url
            # assert 'Services' in self.basePage.get_text(self, FresnoLocators.page_title)
        finally:
            self.driver.close()

    def test_check_single_pages_urls_and_titles(self, setup):
        try:
            self.driver = setup
            self.homePage = HomePage(self.driver, Urls.Fresno)
            self.basePage = BasePage(self.driver)

            self.homePage.click_popup_service(GenericLocators.popup_refrigerator)
            assert 'refrigerator-repair' in self.driver.current_url
            assert 'Refrigerator Repair' in self.basePage.get_text(FresnoLocators.service_title)

            self.homePage.click_popup_service_active(GenericLocators.popup_range)
            assert 'range-hood-repair' in self.driver.current_url
            assert 'Range Hood Repair' in self.basePage.get_text(FresnoLocators.service_title)

            self.homePage.click_popup_service_active(GenericLocators.popup_dryer)
            assert 'dryer-repair' in self.driver.current_url
            assert 'Dryer Repair' in self.basePage.get_text(FresnoLocators.service_title)

            self.homePage.click_popup_service_active(GenericLocators.popup_washer)
            assert 'washer-repair' in self.driver.current_url
            assert 'Washer Repair' in self.basePage.get_text(FresnoLocators.service_title)

            self.homePage.click_popup_service_active(GenericLocators.popup_microwave)
            assert 'microwave-repair' in self.driver.current_url
            assert 'Microwave Repair' in self.basePage.get_text(FresnoLocators.service_title)

            self.homePage.click_popup_service_active(GenericLocators.popup_oven)
            assert 'oven-repair' in self.driver.current_url
            assert 'Oven Repair' in self.basePage.get_text(FresnoLocators.service_title)

            self.homePage.click_popup_service_active(GenericLocators.popup_freezer)
            assert 'freezer-repair' in self.driver.current_url
            assert 'Freezer Repair' in self.basePage.get_text(FresnoLocators.service_title)

            self.homePage.click_popup_service_active(GenericLocators.popup_stove)
            assert 'stove-repair' in self.driver.current_url
            assert 'Stove Repair' in self.basePage.get_text(FresnoLocators.service_title)

            self.homePage.click_popup_service_active(GenericLocators.popup_dishwasher)
            assert 'dishwasher-repair' in self.driver.current_url
            assert 'Dishwasher Repair' in self.basePage.get_text(FresnoLocators.service_title)

            self.homePage.click_popup_service_active(GenericLocators.popup_wine)
            assert 'wine-cooler-repair' in self.driver.current_url
            assert 'Wine Cooler Repair' in self.basePage.get_text(FresnoLocators.service_title)

            self.homePage.click_popup_service_active(GenericLocators.popup_trash)
            assert 'trash-compactor-repair' in self.driver.current_url
            assert 'Trash Compactor Repair' in self.basePage.get_text(FresnoLocators.service_title)

            self.homePage.click_popup_service_active(GenericLocators.popup_garbage)
            assert 'garbage-disposal-repair' in self.driver.current_url
            assert 'Garbage Disposal Repair' in self.basePage.get_text(FresnoLocators.service_title)
        finally:
            self.driver.close()

    # def test_check_read_more_url_and_title(self, setup):
    #     try:
    #         self.driver = setup
    #         self.homePage = HomePage(self.driver)
    #         self.basePage = BasePage(self.driver)
    #
    #         self.homePage.click_read_more()
    #         assert 'wine-cooler-repair' in self.driver.current_url
    #         assert 'Wine Cooler Repair' in self.basePage.get_text(FresnoLocators.service_title)
    #
    #     finally:
    #         self.driver.close()
