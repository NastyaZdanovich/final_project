import time

import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    with webdriver.Chrome(options=options) as driver:
        yield driver





