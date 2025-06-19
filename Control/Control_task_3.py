from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://www.saucedemo.com/")

# авторизация
driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user") # ввод логина
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce") # ввод пароля
driver.find_element(By.CSS_SELECTOR, "#login-button").click()

# добавление товаров в корзину
driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

# переход в корзину
driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container").click()
driver.find_element(By.CSS_SELECTOR, "#checkout").click()

# заполнение формы
driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Vitali") # ввод имени
driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Rebkovets") # ввод фамилии
driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("225708") # ввод индекса
driver.find_element(By.CSS_SELECTOR, "#continue").click()

# Проверка итоговой суммы
result = driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
if (result == "Total: $58.29"):
    print ("Итоговая сумма $58.29")
else:
    print ("Итоговая сумма не соответствует ожидаемой")

sleep(2)
driver.quit()