import pytest
from selenium import webdriver

from pages2.MainShopTask3 import MainShop
from pages2.CartShopTask3 import CartShop
from pages2.ResultShopTask3 import ResultShop


def test_shop():
    browser = webdriver.Chrome()
    main_shop = MainShop(browser)
    main_shop.get_shop()
    main_shop.authorization()
    main_shop.addition()

    cart_shop = CartShop(browser)
    cart_shop.get_cart()
    cart_shop.set_form()

    result_shop = ResultShop(browser)
    result = result_shop.get_result()

    assert result == "Total: $58.29"
    
    browser.quit()

    
    # Запуск автотеста 'pytest ControlTask_3.py'