import pytest
from selenium.webdriver.common.by import By

def test_registration(driver):
    driver.get("https://demoqa.com/automation-practice-form")
    driver.find_element(By.id, "firstName").send_keys("John")
    driver.find_element(By.id, "lastName").send_keys("Doe")
    driver.find_element(By.id, "userEmail").send_keys("john@example.com")
    driver.find_element(By.id, "submit").click()
    assert "Thanks for submitting" in driver.page_source
