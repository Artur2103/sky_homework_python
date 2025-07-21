from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = None


class CheckoutTwoPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def check_total_price(self):
        # Проверка итоговой суммы
        total = self.driver.find_element(
            By.CSS_SELECTOR, ".summary_total_label").text
        return total
