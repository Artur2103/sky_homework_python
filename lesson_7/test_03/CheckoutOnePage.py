from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = None


class CheckoutOnePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def first_name(self):
        # Заполнение поля first-name
        self.driver.find_element(
            By.CSS_SELECTOR, "#first-name").send_keys("Ivan")

    def last_name(self):
        # Заполнение поля last-name
        self.driver.find_element(
            By.CSS_SELECTOR, "#last-name").send_keys("Petrov")

    def postal_code(self):
        # Заполнение поля postal-code
        self.driver.find_element(
            By.CSS_SELECTOR, "#postal-code").send_keys("123456")

    def continue_click(self):
        # Нажатие кнопки Continue
        self.driver.find_element(
            By.CSS_SELECTOR, "#continue").click()
