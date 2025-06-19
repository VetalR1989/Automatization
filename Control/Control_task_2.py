import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def driver():
    # Инициализация драйвера Chrome
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_calculator(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Установка времени задержки
    time = driver.find_element(By.CSS_SELECTOR, "#delay")
    time.clear()
    time.send_keys("45")

    # Выполнение операций
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    # Ожидание появления результата
    waiter = WebDriverWait(driver, 50)
    result = waiter.until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='15']"))
    )

    # Проверка результата
    assert result.text == "15"

# Запуск автотеста 'pytest Control_task_2.py'