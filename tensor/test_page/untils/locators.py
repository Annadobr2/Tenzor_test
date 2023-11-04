from selenium.webdriver.common.by import By

class BasePageLocators:
    LINK_CONTACTS = (By.LINK_TEXT, 'Контакты') # 'Контакты'

class ContactPageLocators:
    LOCAL_REGION = (By.CLASS_NAME, 'sbis_ru-Region-Chooser__text.sbis_ru-link')
    ANOTHER_REGION = (By.CSS_SELECTOR,'#popup > div.controls-Popup.ws-float-area-show-complete.controls_themes__wrapper.controls-Scroll_webkitOverflowScrollingTouch.controls-Popup__lastItem.undefined.controls-Popup_shown > div > div.sbis_ru-Region-Panel > div > ul > li:nth-child(43) > span')
    CITY_ID = (By.ID,'city-id-2')
    TENZOR = ((By.XPATH,'//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a'))
    CITY_XPATH = (By.XPATH,'//*[@id="contacts_list"]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[2]/div/div/div[1]/div[1]')

class DevPageLocators:
    POWER_IN_PEOPLE = (By.CSS_SELECTOR, '#container > div.tensor_ru-content_wrapper > div > div.tensor_ru-Index__block4-bg > div > div > div:nth-child(1) > div > p.tensor_ru-Index__card-title.tensor_ru-pb-16')
    BUTTUM_MORE_DETAILS = (By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a')
    cooki = (By.CLASS_NAME,'tensor_ru-CookieAgreement__close.icon-Close.ws-flex-shrink-0.ws-flexbox.ws-align-items-center')
