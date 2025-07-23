from selenium.webdriver.common.by import By

class MainShop:

    def __init__(self, browser):
        self._driver = browser

    def get_shop(self):
        self._driver.maximize_window()
        self._driver.get("https://www.saucedemo.com/")

    def authorization(self):
        self._driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user") # ввод логина
        self._driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce") # ввод пароля
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    def addition(self):
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()