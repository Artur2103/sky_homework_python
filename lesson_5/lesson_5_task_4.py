from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
firefox_options = webdriver.FirefoxOptions()

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

#зайти на сайт https://the-internet.herokuapp.com/login
driver.get("https://the-internet.herokuapp.com/login")

#поиск поля username и ввод в него значения
user_locator = "#username"
user_field = driver.find_element(By.CSS_SELECTOR, user_locator)
user_field.send_keys("tomsmith")
sleep(2)

#поиск поля password и ввод в него значения
password_locator = "#password"
password_field = driver.find_element(By.CSS_SELECTOR, password_locator)
password_field.send_keys("SuperSecretPassword!")
sleep(2)

#поиск и клик кнопки Login
login_locator = "button.radius"
login_button = driver.find_element(By.CSS_SELECTOR, login_locator)
login_button.click()
sleep(2)

#поиск всплывающей плашки и вывод текстового сообщения с плашки в консоль
flash_locator = "#flash.flash.success"
flash_message = driver.find_element(By.CSS_SELECTOR, flash_locator).text
print(flash_message)

#закрытие браузера
driver.quit()
