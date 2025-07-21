from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = None


class CartPage:
    def __init__(self, driver)-> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def open_cart(self)-> None:
        """
        Эта функция открывает(переходит) на страницу Корзины
        """
        self.driver.find_element(
            By.CSS_SELECTOR, ".shopping_cart_link").click()

    def checkout_click(self)-> None:
        """
        Эта функция производит нажатие кнопки Checkout
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "#checkout").click()
