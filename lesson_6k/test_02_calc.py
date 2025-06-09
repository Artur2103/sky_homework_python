import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    # Настройка драйвера
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    driver.maximize_window()
    yield driver
    driver.quit()

def test_calc(driver):
    # Переход на страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    wait = WebDriverWait(driver, 50)

    # Очистка и заполнение поля ожидания (по локатору #delay )
    driver.find_element(By.CSS_SELECTOR, '#delay').clear()
    driver.find_element(By.CSS_SELECTOR, '#delay').send_keys('45')

    # Нажатие кнопок калькулятора
    driver.find_element(By.XPATH, "//span[@class='btn btn-outline-primary' and text()='7']").click()
    driver.find_element(By.XPATH, "//span[@class='operator btn btn-outline-success' and text()='+']").click()
    driver.find_element(By.XPATH, "//span[@class='btn btn-outline-primary' and text()='8']").click()
    driver.find_element(By.XPATH, "//span[@class='btn btn-outline-warning' and text()='=']").click()

    # Ожидание вывода результата на экране калькулятора
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

    # Проверка результата
    result = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert result == "15"
