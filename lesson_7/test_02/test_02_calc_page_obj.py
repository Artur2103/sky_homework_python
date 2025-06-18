import pytest
from selenium import webdriver
from CalcPage import CalcPage


@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calc(driver):
    calc_page = CalcPage(driver)
    calc_page.open()
    calc_page.delay_input()
    calc_page.click_7()
    calc_page.click_plus()
    calc_page.click_8()
    calc_page.click_equals()
    calc_page.check_result()
