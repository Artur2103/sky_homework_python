import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    # Настройка драйвера
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()),
    )
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calc(driver):
    # Переход на страницу
    driver.get("https://www.saucedemo.com")

    # Заполнение полей авторизации + нажатие кнопки Login
    driver.find_element(
        By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    driver.find_element(
        By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    driver.find_element(
        By.CSS_SELECTOR, "#login-button").click()

    # Добавление товаров в корзину
    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    # Переход в корзину + нажатие кнопки checkout
    driver.find_element(
        By.CSS_SELECTOR, ".shopping_cart_link").click()
    driver.find_element(
        By.CSS_SELECTOR, "#checkout").click()

    # Заполнение формы данными + нажатие кнопки Continue
    driver.find_element(
        By.CSS_SELECTOR, "#first-name").send_keys("Ivan")
    driver.find_element(
        By.CSS_SELECTOR, "#last-name").send_keys("Petrov")
    driver.find_element(
        By.CSS_SELECTOR, "#postal-code").send_keys("123456")
    driver.find_element(
        By.CSS_SELECTOR, "#continue").click()

    # Проверка итоговой суммы
    total = driver.find_element(
        By.CSS_SELECTOR, ".summary_total_label").text
    assert total == "Total: $58.29"
