from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
firefox_options = webdriver.FirefoxOptions()

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

#зайти на сайт http://the-internet.herokuapp.com/inputs
driver.get("http://the-internet.herokuapp.com/inputs")

#поиск поля и ввод в него данных
input_locator = "input"
input_field = driver.find_element(By.CSS_SELECTOR, input_locator)
input_field.send_keys("Sky")
sleep(2)

#отчистка поля ввода
input_field.clear()
sleep(2)

#ввод данных в поле
input_field.send_keys("Pro")
sleep(2)

#закрытие браузера
driver.quit()
