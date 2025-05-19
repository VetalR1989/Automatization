from time import sleep #импортировали метод из пакета
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()

# Выполнение в  Firefox
#Задание 4

for x in range(0, 3):
	driver.get("http://uitestingplayground.com/dynamicid")
	blueButton = "button.btn-primary"
	searchblueButton = driver.find_element(By.CSS_SELECTOR, blueButton)
	searchblueButton.click()
	
sleep(2)
driver.quit()