from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

waiter = WebDriverWait(driver, 20)
waiter.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "#landscape"))
)

award = driver.find_element(By.CSS_SELECTOR, "#award")
src_award = award.get_attribute("src")
print(src_award)

sleep(5)
driver.quit()