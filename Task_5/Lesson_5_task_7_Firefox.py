from time import sleep #импортировали метод из пакета
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()

# Выполнение в  Firefox
#Задание 7

driver.get("http://the-internet.herokuapp.com/inputs")
input = "input[type='number']"
searchInput = driver.find_element(By.CSS_SELECTOR, input)
searchInput.send_keys("1000")
searchInput.clear()
searchInput.send_keys("999")

sleep(2)
driver.quit()