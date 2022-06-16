from Configs.configs import Urls
from Locators.locators import GenericLocators
from Pages.basepage import BasePage
from Pages.schedulepage import SchedulePage
from Pages.homepage import HomePage
from Tests.basetest import BaseTest


class Test_schedule(BaseTest):
    def test_schedule_service(self, setup):
        try:
            self.driver = setup
            self.contactPage = SchedulePage(self.driver, Urls.Clovis)
            self.basePage = BasePage(self.driver)
            self.homePage = HomePage(self.driver, Urls.Clovis)

            self.homePage.click_header_link(GenericLocators.schedule_service_header)
            self.contactPage.fill_schedule_form()
            self.contactPage.click_schedule_service()
            assert 'Thank You For Choosing Us!' in self.basePage.get_text(GenericLocators.contact_confirm_popup)

        finally:
            self.driver.close()
