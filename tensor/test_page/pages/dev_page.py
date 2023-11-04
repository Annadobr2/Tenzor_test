from selenium.webdriver.common.by import By
from config.setting import ROOT_URL
from test_page.pages.base_page import BasePage
from test_page.untils.locators import DevPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DevPage(BasePage):

    def __init__(self, driver, base_url=ROOT_URL):
        super(DevPage, self).__init__(driver, base_url=ROOT_URL)
        # https://tensor.ru/
        self.base_url = 'https://tensor.ru'

    def get_name_block(self):
        return self.find_element(DevPageLocators.POWER_IN_PEOPLE).text
    def click_cooki(self):
        cooki = self.find_element(DevPageLocators.cooki)
        cooki.click()
    def click_more_ditails(self):
        more_ditails = self.find_element(DevPageLocators.BUTTUM_MORE_DETAILS)
        more_ditails.click()

