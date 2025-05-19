from time import sleep #импортировали метод из пакета
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()

# Выполнение в  Firefox
#Задание 5

for y in range(0, 3):
	driver.get("http://uitestingplayground.com/classattr")
	blueButton2 = "button.btn-primary"
	searchblueButton2 = driver.find_element(By.CSS_SELECTOR, blueButton2)
	searchblueButton2.click()
	alert_obj = driver.switch_to.alert 
	alert_obj.accept()
	
sleep(2)
driver.quit()