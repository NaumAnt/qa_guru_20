from selene import browser, be, have

def test_capcha_google():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('sql-ex.ru.').press_enter()
    browser.element('html').should(have.text('Об этой странице'))

#browser.element('[id="search"]').should(have.text('SQL-EX'))


def test_popup_yandex():
    browser.open('https://ya.ru')
    browser.element('[name="text"]').click().type('sqlex').press_enter()
    browser.element('html').should(have.text('Сделайте Яндекс основным поиском'))
    #browser.all('span').by(have.exact_text('Нет, спасибо')).should(be.visible).click()
    #browser.element('[innerHTML="sql-ex.ru"]').click()
