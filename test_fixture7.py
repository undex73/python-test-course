import pytest
import time
from selenium import webdriver


@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(browser, language):
    link = "http://selenium1py.pythonanywhere.com/{}/".format(language)
    browser.get(link)
    time.sleep(5)
    browser.find_element_by_css_selector("#login_link")
