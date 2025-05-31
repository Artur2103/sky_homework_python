from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

#зайти на сайт http://uitestingplayground.com/classattr
driver.get("http://uitestingplayground.com/classattr")
sleep(3)

# поиск и клик по кнопке с классом btn-primary
blue_button = driver.find_element(By.CLASS_NAME, 'btn-primary')
blue_button.click()
sleep(2)

# закрытие браузера
driver.quit()
