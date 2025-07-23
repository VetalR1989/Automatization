from selenium.webdriver.common.by import By

class KalkulatorPage:

    def __init__(self, browser):
        self._driver = browser
        self._driver.maximize_window()
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_time(self):
        time = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        time.clear()
        time.send_keys("45")
        