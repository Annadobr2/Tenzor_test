import json
import pytest
from config.setting import BASE_DIR
from selenium import webdriver

def get_config_file_path():
    return BASE_DIR / 'config' / 'test_config.json'
# @pytest.fixture()
# def root_url():
#     return BASE_LINK

@pytest.fixture
def config(scope = 'session'):
    with open(get_config_file_path()) as config_file:
        config = json.load(config_file)
    return config

def set_options(opts , config):
    if config['mode'] == 'Headless':
        opts.add_argument('--headless=new')

@pytest.fixture
def browser(config):
    if config['browser'] == 'Chrome':
        opts = webdriver.ChromeOptions()
        set_options(opts, config)
        driver = webdriver.Chrome(options=opts)
    else:
        raise Exception('Unknow type of browser')

    yield driver
    driver.quit()