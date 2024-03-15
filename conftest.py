import pytest
from selene import browser

@pytest.fixture(scope='function')
def browser_personal_settings():
    browser.config.base_url = 'https://google.com'
    browser.config.window_height = 1600
    browser.config.window_width = 2560
