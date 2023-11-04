from selenium.webdriver.common.by import By
from config.setting import ROOT_URL
from test_page.pages.base_page import BasePage
from test_page.untils.locators import DevPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AboutPage(BasePage):

    def __init__(self, driver, base_url=ROOT_URL):
        super(AboutPage, self).__init__(driver, base_url=ROOT_URL)
        # https://tensor.ru/
        self.base_url = 'https://tensor.ru/about'

