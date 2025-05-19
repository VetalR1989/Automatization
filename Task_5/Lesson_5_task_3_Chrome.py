from time import sleep #импортировали метод из пакета
from selenium import webdriver
from selenium.webdriver.common.by import By

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

sleep(2)
driver.quit()