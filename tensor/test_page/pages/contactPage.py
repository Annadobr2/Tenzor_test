from selenium.webdriver.common.by import By
from config.setting import ROOT_URL
from test_page.pages.base_page import BasePage
from test_page.untils.locators import ContactPageLocators, ContactPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ContactPage(BasePage):

    def __init__(self, driver, base_url=ROOT_URL):
        super(ContactPage, self).__init__(driver, base_url=ROOT_URL)
        self.base_url = f'{base_url}/contacts'

    def get_local_region(self):
        return self.find_element(ContactPageLocators.LOCAL_REGION).text

    def click_local_region(self):
        local_region = self.find_element(ContactPageLocators.LOCAL_REGION)
        local_region.click()

    def get_partners(self,type_locators):
        if type_locators == 'ID':
            return self.find_element(ContactPageLocators.CITY_ID).text
        elif type_locators == 'XPATH':
            return self.find_element(ContactPageLocators.CITY_XPATH).text


