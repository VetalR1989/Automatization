from time import sleep #импортировали метод из пакета
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window() #открыть окно по размеру экрана

# Выполнение в Chrome
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

sleep(2)
driver.quit()