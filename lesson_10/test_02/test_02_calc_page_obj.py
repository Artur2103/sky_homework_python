import pytest
import allure
from selenium import webdriver
from CalcPage import CalcPage


@pytest.fixture
def driver():
    """
    Фикстура, предоставляющая объект веб-драйвера для теста.
    """
    driver = webdriver.Edge()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()
    
@allure.title("Проверка функционирования калькулятора")
@allure.description("Сложение чисел 7 + 8 = 15 с установкой ожидания результата сложения")
@allure.severity("BLOCKER")
def test_calc(driver):
    calc_page = CalcPage(driver)
    with allure.step("Открытие страницы Калькулятор"):
        calc_page.open()
    with allure.step("Установка ожидания результата"):
        calc_page.delay_input(45)
    with allure.step("Нажатие кнопки 7"):
        calc_page.click_button("7")
    with allure.step("Нажатие кнопки +"):
        calc_page.click_button("+")
    with allure.step("Нажатие кнопки 8"):
        calc_page.click_button("8")
    with allure.step("Нажатие кнопки ="):
        calc_page.click_button("=")
    with allure.step("Получение результата"):
        result = calc_page.check_result()
    with allure.step("Проверка результата"):
        assert result == "15"
