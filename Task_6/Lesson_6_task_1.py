from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("http://uitestingplayground.com/ajax")
driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

driver.implicitly_wait(17)

id_content = driver.find_element(By.CSS_SELECTOR, "#content")
text_p = id_content.find_element(By.CSS_SELECTOR, "p.bg-success").text
print(text_p)

sleep(5)
driver.quit()