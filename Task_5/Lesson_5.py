from time import sleep #импортировали метод из пакета
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window() #открыть окно по размеру экрана

# Выполнение в Chrome
#Задание 3

driver.get("http://the-internet.herokuapp.com/add_remove_elements/") #открыть сайт
Add = "button[onclick='addElement()']" #локатор Add
searchButtonAdd = driver.find_element(By.CSS_SELECTOR, Add) #найти кнопку Add
for x in range(0, 5):
	searchButtonAdd.click() #кликнуть по кнопке Add
Delete = "button[onclick='deleteElement()']" #локатор Delete
searchButtonDelete = driver.find_elements(By.CSS_SELECTOR, Delete) #найти кнопку Delete
print(len(searchButtonDelete))

#Задание 4

for x in range(0, 3):
	driver.get("http://uitestingplayground.com/dynamicid")
	blueButton = "button.btn-primary"
	searchblueButton = driver.find_element(By.CSS_SELECTOR, blueButton)
	searchblueButton.click()

#Задание 5

for y in range(0, 3):
	driver.get("http://uitestingplayground.com/classattr")
	blueButton2 = "button.btn-primary"
	searchblueButton2 = driver.find_element(By.CSS_SELECTOR, blueButton2)
	searchblueButton2.click()
	alert_obj = driver.switch_to.alert 
	alert_obj.accept()

#Задание 6

driver.get("http://the-internet.herokuapp.com/entry_ad")
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.modal")))
close = "div[class='modal-footer']"
searchClose = driver.find_element(By.CSS_SELECTOR, close)
searchClose.click()

#Задание 7

driver.get("http://the-internet.herokuapp.com/inputs")
input = "input[type='number']"
searchInput = driver.find_element(By.CSS_SELECTOR, input)
searchInput.send_keys("1000")
searchInput.clear()
searchInput.send_keys("999")

#Задание 8

driver.get("http://the-internet.herokuapp.com/login")
username = "#username"
searchUsername = driver.find_element(By.CSS_SELECTOR, username)
searchUsername.send_keys("tomsmith")
password = "#password"
searchPassword = driver.find_element(By.CSS_SELECTOR, password)
searchPassword.send_keys("SuperSecretPassword!")
login = "button.radius"
searchButtonLogin = driver.find_element(By.CSS_SELECTOR, login)
searchButtonLogin.click()

sleep(3) #установили «засыпание» браузера
driver.quit()


# Выполнение в  Firefox
#Задание 3
driver = webdriver.Firefox()
driver.maximize_window()

#Задание 3

driver.get("http://the-internet.herokuapp.com/add_remove_elements/") #открыть сайт
Add = "button[onclick='addElement()']" #локатор Add
searchButtonAdd = driver.find_element(By.CSS_SELECTOR, Add) #найти кнопку Add
for x in range(0, 5):
	searchButtonAdd.click() #кликнуть по кнопке Add
Delete = "button[onclick='deleteElement()']" #локатор Delete
searchButtonDelete = driver.find_elements(By.CSS_SELECTOR, Delete) #найти кнопку Delete
print(len(searchButtonDelete))

#Задание 4

for x in range(0, 3):
	driver.get("http://uitestingplayground.com/dynamicid")
	blueButton = "button.btn-primary"
	searchblueButton = driver.find_element(By.CSS_SELECTOR, blueButton)
	searchblueButton.click()

#Задание 5

for y in range(0, 3):
	driver.get("http://uitestingplayground.com/classattr")
	blueButton2 = "button.btn-primary"
	searchblueButton2 = driver.find_element(By.CSS_SELECTOR, blueButton2)
	searchblueButton2.click()
	alert_obj = driver.switch_to.alert 
	alert_obj.accept()

#Задание 6

driver.get("http://the-internet.herokuapp.com/entry_ad")
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.modal")))
close = "div[class='modal-footer']"
searchClose = driver.find_element(By.CSS_SELECTOR, close)
searchClose.click()

#Задание 7

driver.get("http://the-internet.herokuapp.com/inputs")
input = "input[type='number']"
searchInput = driver.find_element(By.CSS_SELECTOR, input)
searchInput.send_keys("1000")
searchInput.clear()
searchInput.send_keys("999")

#Задание 8

driver.get("http://the-internet.herokuapp.com/login")
username = "#username"
searchUsername = driver.find_element(By.CSS_SELECTOR, username)
searchUsername.send_keys("tomsmith")
password = "#password"
searchPassword = driver.find_element(By.CSS_SELECTOR, password)
searchPassword.send_keys("SuperSecretPassword!")
login = "button.radius"
searchButtonLogin = driver.find_element(By.CSS_SELECTOR, login)
searchButtonLogin.click()

sleep(3) #установили «засыпание» браузера
driver.quit()