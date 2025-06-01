from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
firefox_options = webdriver.FirefoxOptions()

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

#зайти на сайт http://uitestingplayground.com/textinput
driver.get("http://uitestingplayground.com/textinput")

#поиск поля ввода
input_field = driver.find_element(By.CSS_SELECTOR, '#newButtonName')

#ввод данных в поле
input_field.send_keys("SkyPro")

#поиск и клик кнопки
button = driver.find_element(By.CSS_SELECTOR, '#updatingButton').click()

#выделение текста с кнопки
txt = driver.find_element(By.CSS_SELECTOR, '#updatingButton').text

#печать текста сообщения
print(txt)

#закрытие браузера
driver.quit()
