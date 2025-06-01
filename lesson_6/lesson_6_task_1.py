from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
firefox_options = webdriver.FirefoxOptions()

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(20)

#зайти на сайт http://uitestingplayground.com/ajax
driver.get("http://uitestingplayground.com/ajax")

#поиск и клик кнопки
button = driver.find_element(By.CSS_SELECTOR, '#ajaxButton').click()

#поиск плашки с сообщением
content = driver.find_element(By.CSS_SELECTOR, '#content')

#выделение текста сообщения с плашки
message = driver.find_element(By.CSS_SELECTOR, 'p.bg-success').text

#печать текста сообщения
print(message)

#закрытие браузера
driver.quit()
