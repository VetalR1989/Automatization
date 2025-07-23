from selenium.webdriver.common.by import By

class ResultShop:

    def __init__(self, browser):
        self._driver = browser

    def get_result(self):
        result = self._driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
        return result