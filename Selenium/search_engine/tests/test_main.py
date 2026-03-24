import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_google_search(driver):
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.name, "q")
    search_box.send_keys("selenium python")
    search_box.send_keys(Keys.RETURN)
    assert "selenium python" in driver.title.lower()
