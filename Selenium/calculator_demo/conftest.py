import pytest
from selenium import webdriver
from selenium.webdriver.safari.options import Options

@pytest.fixture(scope="function")
def driver():
    options = Options()
    driver = webdriver.Safari(options=options)
    yield driver
    driver.quit()
