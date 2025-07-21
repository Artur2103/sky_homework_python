from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = None


class ProductPage:
    def __init__(self, driver)-> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def add_to_cart_backpack(self)-> None:
        """
        Эта добавляет товар Backpack в корзину
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()

    def add_to_cart_bolt_t_shirt(self)-> None:
        """
        Эта добавляет товар Bolt-t-shirt в корзину
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()

    def add_to_cart_onesie(self)-> None:
        """
        Эта добавляет товар Onesie в корзину
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
