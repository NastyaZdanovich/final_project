import pytest
from selenium import webdriver
from source_code.constants import Host
from source_code.pages.main_page import MainPage
from source_code.pages.sign_in_page import SignInPage


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    main_page = MainPage(driver)
    main_page.open(Host.OZ)
    main_page.click_by_xpath(main_page.accept_cookie_xpath)
    return main_page

@pytest.fixture()
def sign_in(driver, main_page):
    main_page.click_by_xpath(main_page.sign_in_xpath)
    sign_in_page = SignInPage(driver)
    sign_in_page.click_by_xpath(sign_in_page.email_registration)
    sign_in_page.fill_in_a_form_to_sign(-1)
    main_page.switch_handler(0)
    text = main_page.get_a_text(main_page.my_oz_xpath)
    assert text == 'Мой OZ'
