from selene import browser, be, have

def test_one(browser_personal_settings):
    browser.open('')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_two(browser_personal_settings):
    browser.open('')
    browser.element('[name="q"]').should(be.blank).type('3645683465734tycgdjfghdjgkud').press_enter()
    browser.element('[id="rso"]').should(have.text('Похоже, по вашему запросу нет полезных результатов'))