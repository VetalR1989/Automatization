from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class KalkulatorOperation:

    def __init__(self, browser):
        self._driver = browser

    def set_operation(self):
        self._driver.find_element(By.XPATH, "//span[text()='7']").click()
        self._driver.find_element(By.XPATH, "//span[text()='+']").click()
        self._driver.find_element(By.XPATH, "//span[text()='8']").click()
        self._driver.find_element(By.XPATH, "//span[text()='=']").click()

        waiter = WebDriverWait(self._driver, 50)
        result = waiter.until(
            EC.visibility_of_element_located((By.XPATH, "//div[text()='15']"))
        )

        return result.text