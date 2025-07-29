import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    # Настройка драйвера
    driver = webdriver.Edge(
        service=EdgeService(EdgeChromiumDriverManager().install())
    )
    driver.maximize_window()
    yield driver
    driver.quit()


def test_fill_form(driver):
    # Переход на страницу
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

    wait = WebDriverWait(driver, 10)

    # Заполнение формы
    driver.find_element(
        By.CSS_SELECTOR, '[name=first-name]').send_keys('Иван')
    driver.find_element(
        By.CSS_SELECTOR, '[name=last-name]').send_keys('Петров')
    driver.find_element(
        By.CSS_SELECTOR, '[name=address]').send_keys('Ленина, 55-3')
    driver.find_element(
        By.CSS_SELECTOR, '[name=e-mail]').send_keys('test@skypro.com')
    driver.find_element(
        By.CSS_SELECTOR, '[name=phone]').send_keys('+7985899998787')
    driver.find_element(
        By.CSS_SELECTOR, '[name=zip-code]').send_keys('')
    driver.find_element(
        By.CSS_SELECTOR, '[name=city]').send_keys('Москва')
    driver.find_element(
        By.CSS_SELECTOR, '[name=country]').send_keys('Россия')
    driver.find_element(
        By.CSS_SELECTOR, '[name=job-position]').send_keys('QA')
    driver.find_element(
        By.CSS_SELECTOR, '[name=company]').send_keys('SkyPro')

    # Ждем, пока кнопка станет кликабельной
    submit_button = wait.until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, "[type=submit]")))

    driver.execute_script("arguments[0].click();", submit_button)

    # Проверка подсветки поля Zip code
    pole_zip_code = driver.find_element(
        By.ID, "zip-code").get_attribute("class")
    assert pole_zip_code == "alert py-2 alert-danger"

    # Проверка подсветки остальных полей
    poles = [
        "#first-name",
        "#last-name",
        "#address",
        "#city",
        "#country",
        "#e-mail",
        "#phone",
        "#company"
        ]
    for pole in poles:
        pole_class = driver.find_element(
            By.CSS_SELECTOR, pole).get_attribute("class")
        assert pole_class == "alert py-2 alert-success"
