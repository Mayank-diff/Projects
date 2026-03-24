import pytest

def test_calculator(driver):
    driver.get("https://julian.barg.de/webapps/calcy/")
    driver.find_element("id", "one").click()
    driver.find_element("id", "add").click()
    driver.find_element("id", "one").click()
    driver.find_element("id", "equals").click()
    result = driver.find_element("id", "display").text
    assert result == "2"
