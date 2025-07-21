from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    def __init__(self, driver)-> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def open(self)-> None:
        """
        Эта функция открывает главную страницу сайта
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    def delay_input(self, delay_value: int)-> None:
        """
        Эта функция для ввода значения времени (в секундах) ожидания вывода ответа калькулятора
        """
        delay = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay.clear()
        delay.send_keys(int(delay_value))

    def click_button(self, button_text: str)-> None:
        """
        Эта функция производит нажатие на заданные кнопки калькулятора
        """
        button = self.driver.find_element(
            By.XPATH, f"//span[contains(text(), '{button_text}')]"
        )
        button.click()

    def check_result(self)->str:
        """
        Это функция проверки результата
        """
        WebDriverWait(self.driver, 45).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), "15"
            )
        )
        result_text = self.driver.find_element(By.CSS_SELECTOR, ".screen").text
        return result_text
