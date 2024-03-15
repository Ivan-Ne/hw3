import pytest
from selene import browser

@pytest.fixture(scope='session')
def browser_personal_settings():
    browser.config.base_url = 'https://google.com'
    browser.config.window_height = 500
    browser.config.window_width = 500
    print('browser opened')

    yield

    print('browser closed')