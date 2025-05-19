from time import sleep #импортировали метод из пакета
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window() #открыть окно по размеру экрана

# Выполнение в Chrome
#Задание 6

driver.get("http://the-internet.herokuapp.com/entry_ad")
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.modal")))
close = "div[class='modal-footer']"
searchClose = driver.find_element(By.CSS_SELECTOR, close)
searchClose.click()

sleep(2)
driver.quit()