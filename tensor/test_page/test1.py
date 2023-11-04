import pytest
import time
from config.setting import BASE_LINK, parametrs
from test_page.pages.main_page import MainPage
from test_page.pages.contactPage import ContactPage
from test_page.pages.dev_page import DevPage
from test_page.pages.about_page import AboutPage
from conf_test import browser, config
from test_page.untils.locators import BasePageLocators, ContactPageLocators, DevPageLocators
from bs4 import BeautifulSoup


# Переключение на новую вкладку
def _switch_to_another_handler (browser, original_page_handler):
    for window_handle in browser.window_handles:
        if window_handle !=original_page_handler:
            browser.switch_to.window(window_handle)
            break

#Проверка изображений заданным параметрам
def check_parametrs(cards, parametrs):
    pictures = []
    for card in cards:
        pictures.append(list([card.get(i) for i in parametrs]))
    one_par = pictures[0]
    return  (all([True for picture in pictures if picture == one_par]))




# Сценарий 1
def test_one(browser):

    main_page = MainPage(browser)
    main_page.navigate_to()
    main_page.go_to_contact_page()
    contact_page = ContactPage(browser)
    time.sleep(1)
    original_page_handler = browser.current_window_handle
    contact_page.click_on(ContactPageLocators.TENZOR)
    _switch_to_another_handler(browser, original_page_handler)
    dev_page = DevPage(browser)

    # п.4 - Проверка наличия блока 'Сила в людях'
    assert dev_page.get_name_block() == 'Сила в людях'

    cooki = dev_page.find_element(DevPageLocators.cooki)
    dev_page.click_cooki()
    dev_page.click_more_ditails()
    about_page = AboutPage(browser)

    # п. 5 - Проверка корректного url
    assert about_page.url_page() == 'https://tensor.ru/about'

    soup = BeautifulSoup(browser.page_source, "html.parser")
    cards = soup.find_all(attrs={'class': 'tensor_ru-About__block3-image new_lazy'})

    # п. 6 - Проверка заданных парметров изображений (высота и ширина)
    assert check_parametrs(cards, parametrs) == True










