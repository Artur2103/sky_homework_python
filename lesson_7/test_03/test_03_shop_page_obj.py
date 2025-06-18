import pytest
from selenium import webdriver
from MainPage import MainPage
from ProductPage import ProductPage
from CartPage import CartPage
from CheckoutOnePage import CheckoutOnePage
from CheckoutTwoPage import CheckoutTwoPage


@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop(driver):
    main_page = MainPage(driver)
    product_page = ProductPage(driver)
    cart_page = CartPage(driver)
    checkout_one_page = CheckoutOnePage(driver)
    checkout_two_page = CheckoutTwoPage(driver)
    main_page.open()
    main_page.input_username()
    main_page.input_password()
    main_page.login_click()
    product_page.add_to_cart_backpack()
    product_page.add_to_cart_bolt_t_shirt()
    product_page.add_to_cart_onesie()
    cart_page.open_cart()
    cart_page.checkout_click()
    checkout_one_page.first_name()
    checkout_one_page.last_name()
    checkout_one_page.postal_code()
    checkout_one_page.continue_click()
    total = checkout_two_page.check_total_price()

    assert total == "Total: $58.29"
