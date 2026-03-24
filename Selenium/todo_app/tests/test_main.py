import pytest

def test_todo_app(driver):
    driver.get("https://lambdatest.github.io/sample-todo-app/")
    driver.find_element("name", "li1").click()
    driver.find_element("name", "li2").click()
    assert "Sample page - lambdatest.com" == driver.title
