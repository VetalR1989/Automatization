from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("http://uitestingplayground.com/textinput")

form_Button = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
form_Button.clear()
form_Button.send_keys("SkyPro")
driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

new_Button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
text_new_Button = new_Button.text

print(text_new_Button)

sleep(5)
driver.quit()