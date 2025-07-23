import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pages2.FormPageTask1 import FormPage
from pages2.ResultPageTask1 import ResultPage


def test_form():
    browser = webdriver.Chrome()
    form_page = FormPage(browser)
    form_page.filling_field()
    form_page.sending()

    result_page = ResultPage(browser)
    zip = result_page.color_zip()
    assert zip == "rgba(132, 32, 41, 1)", "Цвет поля ZIP красный"

    firstName = result_page.color_firstName()
    assert firstName == "rgba(15, 81, 50, 1)", "Цвет поля firstName зеленый"

    lastName = result_page.color_lastName()
    assert lastName == "rgba(15, 81, 50, 1)", "Цвет поля lastName зеленый"

    address = result_page.color_address()
    assert address == "rgba(15, 81, 50, 1)", "Цвет поля address зеленый"

    city = result_page.color_city()
    assert city == "rgba(15, 81, 50, 1)", "Цвет поля city зеленый"

    country = result_page.color_country()
    assert country == "rgba(15, 81, 50, 1)", "Цвет поля country зеленый"

    mail = result_page.color_mail()
    assert mail == "rgba(15, 81, 50, 1)", "Цвет поля mail зеленый"

    phone = result_page.color_phone()
    assert phone == "rgba(15, 81, 50, 1)", "Цвет поля phone зеленый"

    job = result_page.color_job()
    assert job == "rgba(15, 81, 50, 1)", "Цвет поля job зеленый"

    company = result_page.color_company()
    assert company == "rgba(15, 81, 50, 1)", "Цвет поля company зеленый"

    browser.quit()

# Запуск автотеста 'pytest ControlTask_1.py'