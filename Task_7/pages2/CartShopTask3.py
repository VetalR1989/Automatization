from selenium.webdriver.common.by import By

class CartShop:

    def __init__(self, browser):
        self._driver = browser

    def get_cart(self):
        self._driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container").click()
        self._driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    def set_form(self):
        self._driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Vitali") # ввод имени
        self._driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Rebkovets") # ввод фамилии
        self._driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("225708") # ввод индекса
        self._driver.find_element(By.CSS_SELECTOR, "#continue").click()