import pytest
from selene.support.shared import browser


@pytest.fixture(params=["1920x1080", "1280x720"])
def browser_desktop(request):
    browser.config.window_width = int(request.param.split('x')[0])
    browser.config.window_height = int(request.param.split('x')[1])
    yield
    browser.quit()


@pytest.fixture(params=["540x960"])
def browser_mobile(request):
    browser.config.window_width = int(request.param.split('x')[0])
    browser.config.window_height = int(request.param.split('x')[1])
    yield
    browser.quit()
