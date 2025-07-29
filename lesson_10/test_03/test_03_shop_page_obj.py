import allure
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

@allure.title("Проверка функционирования интернет магазина")
@allure.description("Регистрация пользователя, добавление товаров, проверка общей суммы покупок")
@allure.severity("BLOCKER")
def test_shop(driver):
    main_page = MainPage(driver)
    product_page = ProductPage(driver)
    cart_page = CartPage(driver)
    checkout_one_page = CheckoutOnePage(driver)
    checkout_two_page = CheckoutTwoPage(driver)
    with allure.step("Открытие главной страницы магазина"):
        main_page.open()
    with allure.step("Ввод username"):
        main_page.input_username()
    with allure.step("Ввод password"):
        main_page.input_password()
    with allure.step("Нажатие кнопки login"):
        main_page.login_click()
    with allure.step("Добавление товара backpack в корзину"):
        product_page.add_to_cart_backpack()
    with allure.step("Добавление товара bolt_t_shirt в корзину"):
        product_page.add_to_cart_bolt_t_shirt()
    with allure.step("Добавление товара onesie в корзину"):
        product_page.add_to_cart_onesie()
    with allure.step("Открытие страницы Корзина"):
        cart_page.open_cart()
    with allure.step("Нажатие кнопки checkout"):
        cart_page.checkout_click()
    with allure.step("Ввод данных first_name"):
        checkout_one_page.first_name()
    with allure.step("Ввод данных last_name"):
        checkout_one_page.last_name()
    with allure.step("Ввод данных postal_code"):
        checkout_one_page.postal_code()
    with allure.step("Нажатие кнопки continue"):
        checkout_one_page.continue_click()
    with allure.step("Получение суммы покупок"):
        total = checkout_two_page.check_total_price()
    with allure.step("Проверка суммы покупок"):
        assert total == "Total: $58.29"
