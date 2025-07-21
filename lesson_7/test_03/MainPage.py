from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = None


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def open(self):
        # Открытие главной страницы
        self.driver.get("https://www.saucedemo.com")

    def input_username(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "#user-name").send_keys("standard_user")

    def input_password(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "#password").send_keys("secret_sauce")

    def login_click(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "#login-button").click()
