import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

@pytest.fixture(scope="module")
def driver():
    # Инициализация драйвера
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    sleep(2)
    driver.quit()

def test_form(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполнение формы
    driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys("+7985899998787")
    driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']").clear()  # очищаем и оставляем пустым
    driver.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, "input[name='job-position']").send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys("SkyPro")

    # Отправка формы
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Проверка цветов полей
    color_zip = driver.find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property("color")
    assert color_zip == "rgba(132, 32, 41, 1)", "Цвет поля ZIP красный"

    color_firstName = driver.find_element(By.CSS_SELECTOR, "#first-name").value_of_css_property("color")
    assert color_firstName == "rgba(15, 81, 50, 1)", "Цвет поля first name зеленый"

    color_lastName = driver.find_element(By.CSS_SELECTOR, "#last-name").value_of_css_property("color")
    assert color_lastName == "rgba(15, 81, 50, 1)", "Цвет поля last Name зеленый"

    color_address = driver.find_element(By.CSS_SELECTOR, "#address").value_of_css_property("color")
    assert color_address == "rgba(15, 81, 50, 1)", "Цвет поля address зеленый"

    color_city = driver.find_element(By.CSS_SELECTOR, "#city").value_of_css_property("color")
    assert color_city == "rgba(15, 81, 50, 1)", "Цвет поля city зеленый"

    color_country = driver.find_element(By.CSS_SELECTOR, "#country").value_of_css_property("color")
    assert color_country == "rgba(15, 81, 50, 1)", "Цвет поля country зеленый"

    color_mail = driver.find_element(By.CSS_SELECTOR, "#e-mail").value_of_css_property("color")
    assert color_mail == "rgba(15, 81, 50, 1)", "Цвет поля e-mail зеленый"

    color_phone = driver.find_element(By.CSS_SELECTOR, "#phone").value_of_css_property("color")
    assert color_phone == "rgba(15, 81, 50, 1)", "Цвет поля phone зеленый"

    color_job = driver.find_element(By.CSS_SELECTOR, "#job-position").value_of_css_property("color")
    assert color_job == "rgba(15, 81, 50, 1)", "Цвет поля Job position зеленый"

    color_company = driver.find_element(By.CSS_SELECTOR, "#company").value_of_css_property("color")
    assert color_company == "rgba(15, 81, 50, 1)", "Цвет поля company зеленый"

# Запуск автотеста 'pytest Control_task_1.py'