from config.setting import ROOT_URL
from test_page.pages.base_page import BasePage

from test_page.untils.locators import BasePageLocators, ContactPageLocators

class MainPage(BasePage):

    def __init__(self, driver, base_url=ROOT_URL):
        super(MainPage, self).__init__(driver, base_url=ROOT_URL)
        self.base_url = f'{base_url}'

    def go_to_contact_page(self):
        self.click_on(BasePageLocators.LINK_CONTACTS)
