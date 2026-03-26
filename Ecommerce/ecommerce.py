import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.safari.options import Options

driver = None

def take_screenshot(name):
    if driver:
        os.makedirs("output", exist_ok=True)
        driver.get_screenshot_as_file(f"output/{name}.png")
        print(f"📸 Saved {name}.png")

class BasePage:
    def __init__(self, drv):
        self.driver = drv
        self.wait = WebDriverWait(drv, 25)

    def safe_click(self, locator):
        elem = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", elem)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", elem)
        time.sleep(2)

    def type_text(self, locator, text):
        elem = self.wait.until(EC.visibility_of_element_located(locator))
        elem.clear()
        elem.send_keys(text)

class LoginPage(BasePage):
    SITE_URL = "https://www.saucedemo.com/"
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")

    def login(self):
        global driver
        self.driver.get(self.SITE_URL)
        time.sleep(4)
        self.type_text(self.USERNAME, "standard_user")
        self.type_text(self.PASSWORD, "secret_sauce")
        self.safe_click(self.LOGIN_BTN)
        driver = self.driver
        time.sleep(3)
        print("✅ Login done")

class ProductsPage(BasePage):
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def add_items(self):
        time.sleep(3)
        # Just backpack to avoid bike light issue
        self.safe_click(self.ADD_BACKPACK)
        time.sleep(3)
        print("✅ Backpack added")

    def go_cart(self):
        time.sleep(3)
        self.safe_click(self.CART_ICON)
        time.sleep(3)
        print("✅ Cart page")

class CartPage(BasePage):
    CHECKOUT_BTN = (By.ID, "checkout")

    def checkout(self):
        time.sleep(3)
        self.safe_click(self.CHECKOUT_BTN)

class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    FINISH = (By.ID, "finish")

    def finish(self):
        self.type_text(self.FIRST_NAME, "Test")
        self.type_text(self.LAST_NAME, "User")
        self.type_text(self.ZIP, "12345")
        self.safe_click(self.CONTINUE)
        time.sleep(2)
        self.safe_click(self.FINISH)
        print("✅ Order finished!")

# Run
options = Options()
driver = webdriver.Safari(options=options)

try:
    login = LoginPage(driver)
    login.login()
    take_screenshot("products")

    products = ProductsPage(driver)
    products.add_items()
    take_screenshot("after_add")

    products.go_cart()
    take_screenshot("cart")

    cart = CartPage(driver)
    cart.checkout()

    checkout = CheckoutPage(driver)
    checkout.finish()
    take_screenshot("done")

    print("🎉 SauceDemo SUCCESS! 5 PNGs saved.")

except Exception as e:
    print(f"Error: {e}")
    take_screenshot("error")

finally:
    time.sleep(5)
    driver.quit()
