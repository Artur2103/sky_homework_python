from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = None


class CalcPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def open(self):
        # Открытие главной страницы
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
            )

    def delay_input(self):
        # Очистка и заполнение поля ожидания (по локатору #delay )
        delay = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay.clear()
        delay.send_keys("45")

    def click_7(self):
        # Нажатие кнопки "7"
        self.driver.find_element(
            By.XPATH, "//span[@class='btn btn-outline-primary' and text()='7']"
            ).click()

    def click_plus(self):
        # Нажатие кнопки "+"
        self.driver.find_element(
            By.XPATH,
            "//span[@class='operator btn btn-outline-success' and text()='+']"
            ).click()

    def click_8(self):
        # Нажатие кнопки "8"
        self.driver.find_element(
            By.XPATH,
            "//span[@class='btn btn-outline-primary' and text()='8']"
            ).click()

    def click_equals(self):
        # Нажатие кнопки "="
        self.driver.find_element(
            By.XPATH,
            "//span[@class='btn btn-outline-warning' and text()='=']"
            ).click()

    def check_result(self):
        WebDriverWait(self.driver, 45).until(

            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR, ".screen"), "15")

        )
        result_text = self.driver.find_element(By.CSS_SELECTOR, ".screen").text
        return result_text
