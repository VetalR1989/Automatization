import pytest
from selenium import webdriver
from pages2.KalkulatorPageTask2 import KalkulatorPage
from pages2.KalkulatorOperationTask2 import KalkulatorOperation


def test_calculator():
    browser = webdriver.Chrome()
    kalkulator_page = KalkulatorPage(browser)
    kalkulator_page.set_time()

    kalkulator_operation = KalkulatorOperation(browser)
    sum = kalkulator_operation.set_operation()

    assert sum == "15"

    browser.quit()

# Запуск автотеста 'pytest ControlTask_2.py'