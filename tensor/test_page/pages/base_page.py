from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.setting import ROOT_URL
import requests
from test_page.conf_test import browser, config
class BasePage:

    def __init__(self, driver, base_url=ROOT_URL):
        self.driver = driver
        self.base_url = base_url

    def find_element(self,locator, timeout_sec=10):
        return WebDriverWait(self.driver,timeout_sec).until(EC.presence_of_element_located(locator))

    # def find_elements(self,locator, timeout_sec=10):
    #     return WebDriverWait(self.driver,timeout_sec).until(EC.presence_of_all_elements_located(locator))

    def click_on(self,locator):
        self.find_element(locator).click()

    def navigate_to(self,url=''):
        url_to = self.base_url + url
        self.driver.get(url_to)

    def get_title(self):
        return self.driver.title


    def wait_until_visibility_of_element_located(self,locator):
        WebDriverWait(self.driver, timeout=5).until(EC.visibility_of_element_located())

    def url_page(self):
        url_p = self.driver.current_url
        return url_p
