from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = None


class CheckoutOnePage:
    def __init__(self, driver)-> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def first_name(self)-> None:
        """
        Эта функция вводит значение Ivan в поле first-name
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "#first-name").send_keys("Ivan")

    def last_name(self)-> None:
        """
        Эта функция вводит значение Petrov в поле last-name
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "#last-name").send_keys("Petrov")

    def postal_code(self)-> None:
        """
        Эта функция вводит значение 123456 в поле postal-code
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "#postal-code").send_keys("123456")

    def continue_click(self)-> None:
        """
        Эта функция производит нажатие кнопки Continue
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "#continue").click()
