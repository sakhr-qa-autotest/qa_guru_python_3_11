import pytest
from selene import have
from selene.support.shared import browser


@pytest.mark.parametrize('browser_mobile', ["540x960"], indirect=True)
def test_github_mobile_indirect(browser_mobile):
    browser.open('https://github.com')
    browser.element('div>[aria-label="Toggle navigation"]').click()
    browser.element('a[href="/login"]').click()
    browser.element('.auth-form-header').should(have.text("Sign in to GitHub"))


@pytest.mark.parametrize('width, height', [
    pytest.param(1920, 1080, id='Browser size: 1920x1080'),
    pytest.param(768, 1024, id='Browser size: 768x1024')
])
def test_github_mobile(browser_mobile, width, height):
    if width == 1920:
        pytest.skip("Недопустимый разрешение экрана")
    else:
        browser.open('https://github.com')
        browser.driver.set_window_size(width, height)
        browser.element('div>[aria-label="Toggle navigation"]').click()
        browser.element('a[href="/login"]').click()
        browser.element('.auth-form-header').should(have.text("Sign in to GitHub"))
