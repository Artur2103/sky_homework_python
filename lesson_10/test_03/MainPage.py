from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = None


class MainPage:
    def __init__(self, driver)-> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def open(self)-> None:
        """
        Эта функция открывает главную страницу сайта
        """
        self.driver.get("https://www.saucedemo.com")

    def input_username(self)-> None:
        """
        Эта функция вводит значение standard_user в поле user-name
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "#user-name").send_keys("standard_user")

    def input_password(self)-> None:
        """
        Эта функция вводит значение secret_sauce в поле password
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "#password").send_keys("secret_sauce")

    def login_click(self)-> None:
        """
        Эта функция производит нажатие кнопки Login
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "#login-button").click()
