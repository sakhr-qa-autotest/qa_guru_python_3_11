import pytest
from selene import have
from selene.support.shared import browser


@pytest.mark.parametrize('browser_desktop', ["1440x900"], indirect=True)
def test_github_desktop_indirect(browser_desktop):
    browser.open('https://github.com')
    browser.element('a[href="/login"]').click()
    browser.element('.auth-form-header').should(have.text("Sign in to GitHub"))


@pytest.mark.parametrize('width, height', [
    pytest.param(1600, 1200, id='Browser size: 1600x1200'),
    pytest.param(540, 960, id='Browser size: 540x960')
])
def test_github_desktop(browser_desktop, width, height):
    if width == 540:
        pytest.skip("Недопустимый разрешение экрана")
    else:
        browser.open('https://github.com')
        browser.driver.set_window_size(width, height)
        browser.element('a[href="/login"]').click()
        browser.element('.auth-form-header').should(have.text("Sign in to GitHub"))
