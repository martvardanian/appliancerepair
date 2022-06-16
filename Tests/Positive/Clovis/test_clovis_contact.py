from Locators.locators import GenericLocators
from Pages.basepage import BasePage
from Pages.contactpage import ContactPage
from Pages.homepage import HomePage
from Tests.basetest import BaseTest
from Configs.configs import Urls


class Test_contact(BaseTest):
    def test_contact_us(self, setup):
        try:
            self.driver = setup
            self.contactPage = ContactPage(self.driver, Urls.Clovis)
            self.basePage = BasePage(self.driver)
            self.homePage = HomePage(self.driver, Urls.Clovis)

            self.homePage.click_header_link(GenericLocators.contact_header)
            self.contactPage.fill_contact_form()
            self.contactPage.send_contact()
            assert 'Thank you for contacting us!' in self.basePage.get_text(GenericLocators.contact_confirm_popup)

        finally:
            self.driver.close()
