import pytest
import time
from config.setting import BASE_LINK
from test_page.pages.main_page import MainPage
from test_page.pages.contactPage import ContactPage
from conf_test import browser, config
from test_page.untils.locators import BasePageLocators, ContactPageLocators


def test_two(browser):
    main_page = MainPage(browser)
    main_page.navigate_to()
    main_page.go_to_contact_page()
    contact_page = ContactPage(browser)

    # п. 2 - проверка определения местоположения. В данном тесте расматривается г. Санкт-Петербург.
    assert contact_page.get_local_region() == 'г. Санкт-Петербург'
    # п. 2 - проверка определения местоположения списка партнеров.
    assert contact_page.get_partners('XPATH') == 'СБИС - Санкт-Петербург'

    contact_page.click_local_region()
    contact_page.click_on(ContactPageLocators.ANOTHER_REGION)
    time.sleep(2)

    # п. 3 - проверка на изменение выбранного региона. В данном случае 'Камчатский край'.
    assert contact_page.get_local_region() == 'Камчатский край'
    # п. 4 - проверка на отображение вернрго url
    assert 'kamchatskij-kraj' in contact_page.url_page()
    # п. 4 - проверка на отображение вернрго title
    assert contact_page.get_title() == 'СБИС Контакты — Камчатский край'
    # п. 4 - проверка на изменение списка партнеров
    assert contact_page.get_partners('ID') == 'Петропавловск-Камчатский'





