from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = None


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def open_cart(self):
        # Переход в корзину
        self.driver.find_element(
            By.CSS_SELECTOR, ".shopping_cart_link").click()

    def checkout_click(self):
        # Нажатие кнопки Checkout
        self.driver.find_element(
            By.CSS_SELECTOR, "#checkout").click()
